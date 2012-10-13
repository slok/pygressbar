import random
import time

from pygressbar import (SimpleProgressBar,
                        CustomProgressBar,
                        SimplePercentProgressBar)


def show_simple_animation():
    bar = SimpleProgressBar()
    bar.show_progress_bar()
    while(not bar.completed()):
        time.sleep(0.1)
        bar.increase(5)
        bar.show_progress_bar()


def show_custom_animation():
    total = 50
    fill_char = 'x'
    empty_char = '.'
    head = None
    left_limit = '['
    right_limit = ']'
    scale_start = 0
    scale_end = 1000
    bar = CustomProgressBar(length=total,
                            left_limit=left_limit,
                            right_limit=right_limit,
                            head_repr=head,
                            empty_repr=empty_char,
                            filled_repr=fill_char,
                            start=0,
                            scale_start=scale_start,
                            scale_end=scale_end)
    bar.show_progress_bar()
    while(not bar.completed()):
        time.sleep(0.03)
        bar.increase(10)
        bar.show_progress_bar()


def show_simple_percent_animation():
    bar = SimplePercentProgressBar()
    bar.show_progress_bar()
    while(not bar.completed()):
        time.sleep(0.3)
        bar.increase(random.randint(1, 10))
        bar.show_progress_bar()


def show_up_down_animation():
    bar = SimplePercentProgressBar()
    bar.show_progress_bar()

    up = False

    for i in range(5):

        if up:
            up = False
            bar.decrease(1)
        else:
            up = True
            bar.increase(1)

        while(bar.progress > 0 and bar.progress < 100):
            time.sleep(0.1)
            factor = random.randint(1, 10)
            if up:
                bar.increase(factor)
            else:
                bar.decrease(factor)
            bar.show_progress_bar()

if __name__ == "__main__":
    print("Simple bar: ")
    show_simple_animation()
    print("")

    print("Custom bar: ")
    show_custom_animation()
    print("")

    print("Simple with percent bar: ")
    show_simple_percent_animation()
    print("")

    print("Increase and decrease bar: ")
    show_up_down_animation()
    print("")
