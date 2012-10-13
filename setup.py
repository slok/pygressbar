try:
    from setuptools import setup, find_packages
    kw = {'packages': find_packages(exclude=['tests']),
          'test_suite': 'tests',
          'zip_safe': False}
except ImportError:
    from distutils.core import setup
    kw = {'scripts': ['pygressbar.py']}

setup(
    name='pygressbar',
    version='0.1',
    url='https://github.com/slok/pygressbar',
    license='BSD',
    author='Xabier Larrakoetxea',
    author_email='slok69@gmail.com',
    description='Pygressbar is a command line progress bar creator',
    long_description=('Pygressbar is a command line progress bar creation '
                      'utility. Is customizable, flexible and extensible '
                      'the creation of new progress bars is very easy'),
    py_modules=['pygressbar'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    **kw
)
