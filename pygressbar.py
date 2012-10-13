import sys
import abc

if sys.hexversion < 0x020700f0:  # hex number for 2.7.0 final release
    sys.exit("Python 2.7.0 or newer is required to run this program.")


class PygressBar(object):
    """Progress bar abstract base class"""

    __metaclass__ = abc.ABCMeta

    def __init__(self, length, filled_repr, empty_repr, left_limit, right_limit,
                 start, head_repr, format, scale_start, scale_end):
        """Constructor of the abstract base class

        :param length: The length of the bar (without limits)
        :type length: int
        :param filled_repr: This will be represent one filled space
        :type filled_repr: string
        :param empty_repr: This will be represent one empty space
        :type empty_repr: string
        :param left_limit: The limit representation of the left side
        :type left_limit: string
        :param right_limit: The limit representation of the right side
        :type right_limit: string
        :param start: The point the progress bar progress will start
        :type start: int
        :param head_repr: The representation space of the head (Coul be None)
        :type head_repr: string
        :param format: The format of the bar (By default there is one)
        :type format: string
        :param scale_start: The scale number where starts
        :type scale_start: int
        :param scale_end: The scale number where ends
        :type scale_end: int
        """
        self._length = length
        self._filled_repr = filled_repr
        self._empty_repr = empty_repr
        self._left_limit = left_limit
        self._right_limit = right_limit
        self._head_repr = head_repr
        self._start = start
        self._progress = self._start

        #Check the scale
        if scale_start >= scale_end:
            raise ValueError("scale start must be less than scale end")

        self._scale_start = scale_start
        self._scale_end = scale_end
        if not format:
            self._format = "{left_limit}{{:{filled_repr}>{filled_length}}}" +\
                            "{{:{empty_repr}<{empty_length}}}{right_limit}"
        else:
            self._format = format
        # Initialize progress bar
        self._progress_bar = None
        self._make_progress_bar()

    @abc.abstractmethod
    def _create_bar_format(self, filled_length, empty_length):
        """Creates the format of the bar ready to fill in

        :param filled_length: The length of the filled area
        :type filled_length: int
        :param empty_length: The length of the empty area
        :type empty_length: int
        """
        # Create the formatting string for the bar
        return self._format.format(left_limit=self._left_limit,
                                   filled_repr=self._filled_repr,
                                   filled_length=filled_length,
                                   empty_repr=self._empty_repr,
                                   empty_length=empty_length,
                                   right_limit=self._right_limit)

    def _make_progress_bar(self):
        """Creates the progress bar based on the object information and stores
        the bar in the object
        """

        # Create the length of the bar (0 to 100)
        scale = self._scale_end - self._scale_start
        filled_length = (self._length * self._progress // scale)

        # Get the head char. This depends on the progress of the bar
        # If the filled lenght is 0 (0 chars) then is no head nor body
        if not filled_length:
            head = ''
        else:  # If there is no head, then is the fill char representation
            head = self._filled_repr if not self._head_repr else self._head_repr

        # The rest of the bar
        empty_length = self._length - filled_length

        #create the format
        repr_format_str = self._create_bar_format(filled_length, empty_length)

        # Create the progress bar (right head char is always blank)
        self._progress_bar = repr_format_str.format(head, '')

    def increase(self, incr):
        """Increases by a number the progress bar"""
        self._progress += incr

        # Check bounds
        if self._progress > self._scale_end:
            self._progress = self._scale_end

        self._make_progress_bar()  # Update

    def decrease(self, incr):
        """decreases by a number the progress bar"""
        self._progress -= incr

        # Check bounds
        if self._progress < self._scale_start:
            self._progress = self._scale_start

        self._make_progress_bar()

    def completed(self):
        """Returns true if the progress has finished"""
        return self._progress >= self._scale_end

    def show_progress_bar(self):
        """Prints in the terminal the progress bar. valid for animation"""
        if sys.stderr.isatty():
            sys.stderr.write(self.progress_bar + '\r')
        else:
            print(self.progress_bar + "\n")

    def __str__(self):
        return self.progress_bar

    @property
    def progress_bar(self):
        return self._progress_bar

    @property
    def progress(self):
        return self._progress


class SimpleProgressBar(PygressBar):
    def __init__(self):
        super(SimpleProgressBar, self).__init__(length=20,
                                               filled_repr='=',
                                               empty_repr=' ',
                                               left_limit='[',
                                               right_limit=']',
                                               start=0,
                                               head_repr='>',
                                               format=None,
                                               scale_start=0,
                                               scale_end=100)

    def _create_bar_format(self, filled_length, empty_length):
        return super(SimpleProgressBar, self)._create_bar_format(filled_length,
                                                                 empty_length)


class SimplePercentProgressBar(PygressBar):
    def __init__(self):
        super(SimplePercentProgressBar, self).__init__(length=20,
                                                       filled_repr='=',
                                                       empty_repr=' ',
                                                       left_limit='[',
                                                       right_limit=']',
                                                       start=0,
                                                       head_repr='>',
                                                       format=None,
                                                       scale_start=0,
                                                       scale_end=100)

    def _create_bar_format(self, filled_length, empty_length):
        scale = self._scale_end - self._scale_start
        percent = 100 * self._progress // scale
        percent = 100 if percent > 100 else percent  # Not greater than 100
        percent = "({0}%)".format(percent)

        return self._format.format(left_limit=self._left_limit,
                                   filled_repr=self._filled_repr,
                                   filled_length=filled_length,
                                   empty_repr=self._empty_repr,
                                   empty_length=empty_length,
                                   right_limit=self._right_limit) + percent


class CustomProgressBar(PygressBar):
    def __init__(self,
                length,
                filled_repr,
                empty_repr,
                left_limit,
                right_limit,
                start,
                head_repr,
                scale_start,
                scale_end):
        super(CustomProgressBar, self).__init__(length=length,
                                                filled_repr=filled_repr,
                                                empty_repr=empty_repr,
                                                left_limit=left_limit,
                                                right_limit=right_limit,
                                                start=start,
                                                head_repr=head_repr,
                                                format=None,
                                                scale_start=scale_start,
                                                scale_end=scale_end)

    def _create_bar_format(self, filled_length, empty_length):
        return super(CustomProgressBar, self)._create_bar_format(filled_length,
                                                                 empty_length)
