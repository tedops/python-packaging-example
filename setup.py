from setuptools import setup

setup(
    name = "printer",
    packages = ["printer"],
    entry_points = {
        "console_scripts": ['printer = printer.printer:main']
        },
    version = "0.0.3",
    description = "Python command line application that prints a word.",
    long_description = "This is a sample program to demonstrate packaging a cli script.",
    author = "Your Name",
    author_email = "your@mail.com",
    url = "https://github.com/tedops/python-packaging-example",
)
