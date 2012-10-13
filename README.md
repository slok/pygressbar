PygressBar
==========

[![Build Status](https://secure.travis-ci.org/slok/pygressbar.png)](http://travis-ci.org/slok/pygressbar)

Description
-----------

PygressBar is a progressbar utility for our command line tools, 
scripts... Some of features:

* Different flavours with premade bars
* Extensible
* Customizable bars
* Fast and easy usage
* Terminal bar animation compatible (wget style)
* Python 3 compatible

Requirements
------------
* Python >=2.7 or Python 3


Bar flavours
-----------

###Simple bar###

The simple bar is a bar that its head is `>` its body area is `=` and 
the empty area is ` `. It's length always is 20. Example

    [==============>     ]


###Custom bar###

The custom bar, is a bar that can be customized in all the ways.

* Left and right limits
* Lenght
* Fill char
* Empty char
* Head
* Format
* Scale (for increase and decrease)
* Start point

Some examples:

    (==============#..................................)
    |#####@-----------|
    <xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxO____________>
    #------->**************#
    ||||||||||||||||||||||_________


###Simple percent bar###

The simple percent bar is the same as the simple bar, but in the right side
has the numeric percent progress. Example

    [===================>](100%)
    [>                   ](5%)
    [=========>          ](54%)
    [======>             ](36%)
    [===========>        ](63%)


Usage
-----

The usage is very simple. Create an instance of the bar that you want:

    >>> bar = SimpleProgressBar()

Now we can obtain the progress of the bar

    >>> bar.progress  
    0

And increase and decrease

    >>> bar.increase(50)
    >>> bar.progress
    50
    >>> bar.decrease(3) 
    >>> bar.progress
    47

If we want we can obtain the progress bar representation

    >>> bar.progress_bar
    '[========>           ]'

If we want to animate the bar in the terminal, we can print it directly. This
allows to animate if we don't print nothing more after printing this.

    >>> bar.show_progress_bar()
    [========>           ]

Example
-------

Download a big txt file (12 MB):

    def download_file():
        big_file_url = "https://gist.github.com/raw/3885120/803c00" +\
                       "b809c7a9c4a44626320374d18933b63b48/big.txt"

        # Download the file
        if sys.version_info[0] == 3:
            f = urllib.request.urlopen(big_file_url)
        else:
            f = urllib.urlopen(big_file_url)

        # Get the total length of the file
        scale = int(f.headers["content-length"])
        chunk_size = 500

        bar = CustomProgressBar(length=50,
                                left_limit='[',
                                right_limit=']',
                                head_repr=None,
                                empty_repr=' ',
                                filled_repr='|',
                                start=0,
                                scale_start=0,
                                scale_end=scale)

        print("Downloading a big txt file: ")

        print_flag = 0
        # Load all the data chunk by chunk
        while not bar.completed():
            f.read(chunk_size)
            bar.increase(chunk_size)

            # Don't print always
            if print_flag == 100:
                bar.show_progress_bar()
                print_flag = 0
            else:
                print_flag += 1

        bar.show_progress_bar()
        print("")
        print("Finished :)")


Author
------

Xabier (slok) Larrakoetxea - (slok69 [at] gmail.com)

License
-------
3 clause/New BSD license: 
[opensource](http://www.opensource.org/licenses/BSD-3-Clause), 
[wikipedia](http://en.wikipedia.org/wiki/BSD_licenses)
