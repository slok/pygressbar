import unittest

from pygressbar import (SimpleProgressBar,
                        CustomProgressBar,
                        SimplePercentProgressBar)


class TestPygressBar(unittest.TestCase):

    def format_string(self, total, left_limit, right_limit, fill_char,
                        empty_char, head):
        return "{0}{1}{2}{3}{4}".format(left_limit,
                                        fill_char * (total // 2 - len(head)),
                                        head,
                                        empty_char * (total // 2),
                                        right_limit)

    def test_empty_bar(self):
        """Tests the default empty progress bar"""
        total = 20
        bar = SimpleProgressBar()
        self.assertEqual("[{0}]".format(' ' * total,), bar.progress_bar)
        #print("Result for 0%: " + bar.progress_bar)

    def test_50_percent_bar(self):
        """Tests the default 50 percent progress bar"""
        total = 20
        bar = SimpleProgressBar()
        bar.increase(50)
        self.assertEqual("[{0}>{1}]".format('=' * (total // 2 - 1),
                                            ' ' * (total // 2)),
                                            bar.progress_bar)
        #print("Result for 50%: " + bar.progress_bar)

    def test_100_percent_bar(self):
        """Tests the default 100 percent progress bar"""
        total = 20
        bar = SimpleProgressBar()
        bar.increase(100)
        self.assertEqual("[{0}>{1}]".format('=' * (total - 1), ''),
                                            bar.progress_bar)
        #print("Result for 100%: " + bar.progress_bar)

    def test_complete_query_percent_bar(self):
        """Tests the query of complete or not complete"""
        bar = SimpleProgressBar()
        bar.increase(100)
        self.assertTrue(bar.completed())

        bar = SimpleProgressBar()
        bar.increase(99)
        self.assertFalse(bar.completed())

    def test_incr_10_percent_bar(self):
        """Tests the default bar one by one"""
        bar = SimpleProgressBar()
        incr_factor = 1
        total = 20
        scale = 100
        while not bar.completed():
            total_progress = bar.progress + incr_factor
            bar.increase(incr_factor)

            filled = total * total_progress // scale
            empty = total - filled

            # Custoize The head
            char = '>' if filled > 0 else ''

            test_bar = "[{0}{1}{2}]".format('=' * (filled - 1),
                                            char,
                                            ' ' * empty)

            self.assertEqual(test_bar, bar.progress_bar)
            #print("Result for {0}%: {1}".format(total_progress,
            #                                    bar.progress_bar))

    def test_decrease_bar(self):
        """Tests the decrement of the bar"""
        total = 20
        bar = SimpleProgressBar()
        bar.increase(50)
        self.assertEqual("[{0}>{1}]".format('=' * (total // 2 - 1),
                                            ' ' * (total // 2)),
                                            bar.progress_bar)

        bar.decrease(10)
        self.assertEqual("[{0}>{1}]".format('=' * (total // 2 - 3),
                                            ' ' * (total // 2 + 2)),
                                            bar.progress_bar)

    def test_custom_bar(self):
        """Test a custom progress bar"""
        total = 100
        fill_char = '#'
        empty_char = '.'
        head = '|'
        left_limit = '('
        right_limit = ')'
        scale_start = 0
        scale_end = 100
        bar = CustomProgressBar(length=total,
                                left_limit=left_limit,
                                right_limit=right_limit,
                                head_repr=head,
                                empty_repr=empty_char,
                                filled_repr=fill_char,
                                start=0,
                                scale_start=scale_start,
                                scale_end=scale_end)

        bar.increase((scale_end - scale_start) // 2)
        test_str = self.format_string(total, left_limit, right_limit, fill_char,
                                    empty_char, head)
        self.assertEqual(test_str, bar.progress_bar)

        #print("Result for custom 50%: " + bar.progress_bar)

    def test_custom_bar_without_head(self):
        """Test a custom progress bar without head"""

        total = 50
        fill_char = '#'
        empty_char = ' '
        head = None
        left_limit = '['
        right_limit = ']'
        scale_start = 0
        scale_end = 100
        bar = CustomProgressBar(length=total,
                                left_limit=left_limit,
                                right_limit=right_limit,
                                head_repr=head,
                                empty_repr=empty_char,
                                filled_repr=fill_char,
                                start=0,
                                scale_start=scale_start,
                                scale_end=scale_end)

        head = fill_char if not head else head
        bar.increase((scale_end - scale_start) // 2)
        test_str = self.format_string(total, left_limit, right_limit, fill_char,
                                    empty_char, head)
        self.assertEqual(test_str, bar.progress_bar)

        #print("Result for custom 50%: " + bar.progress_bar)

    def test_custom_bar_with_triple_head(self):
        """Test a custom progress bar with a triple head"""

        total = 100
        fill_char = '='
        empty_char = ' '
        head = '>>>'
        left_limit = '['
        right_limit = ']'
        scale_start = 0
        scale_end = 100
        bar = CustomProgressBar(length=total,
                                left_limit=left_limit,
                                right_limit=right_limit,
                                head_repr=head,
                                empty_repr=empty_char,
                                filled_repr=fill_char,
                                start=0,
                                scale_start=scale_start,
                                scale_end=scale_end)

        head = fill_char if not head else head
        bar.increase((scale_end - scale_start) // 2)
        test_str = self.format_string(total, left_limit, right_limit, fill_char,
                                    empty_char, head)
        self.assertEqual(test_str, bar.progress_bar)

        #print("Result for custom 50%: " + bar.progress_bar)

    def test_custom_bar_with_scale(self):
        """Test a custom progress bar with a custom scale"""

        total = 50
        fill_char = '#'
        empty_char = ' '
        head = '>'
        left_limit = '['
        right_limit = ']'
        scale_start = 415
        scale_end = 431
        bar = CustomProgressBar(length=total,
                                left_limit=left_limit,
                                right_limit=right_limit,
                                head_repr=head,
                                empty_repr=empty_char,
                                filled_repr=fill_char,
                                start=0,
                                scale_start=scale_start,
                                scale_end=scale_end)

        head = fill_char if not head else head
        bar.increase((scale_end - scale_start) // 2)
        test_str = self.format_string(total, left_limit, right_limit, fill_char,
                                    empty_char, head)
        self.assertEqual(test_str, bar.progress_bar)
        #print("Result for custom 50%: " + bar.progress_bar)

    def test_simple_bar_with_percent(self):
        """Tests the simple percent animation bar"""
        total = 20
        bar = SimplePercentProgressBar()
        bar.increase(50)
        self.assertEqual("[{0}>{1}]({2}%)".format('=' * (total // 2 - 1),
                                                  ' ' * (total // 2),
                                                  100 * (total // 2) // total),
                                            bar.progress_bar)
        #print("Result for 100%: " + bar.progress_bar)

if __name__ == '__main__':
    unittest.main()
