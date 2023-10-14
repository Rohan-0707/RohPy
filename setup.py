from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A basic package to learn Python with any Interrupt'
LONG_DESCRIPTION = "A basic Package, which install some of required or necessary libraries as per users learning level of Python ! When user install this package, then they will doesn't need to install external package manually. It will automatically install some of important packages to make learnig easier !"

# Setting up
setup(
    name="RohPy",
    version=VERSION,
    author="Rohan Kumar Bhoi (Rohan-0707)",
    author_email="<rohanbhoi1546@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['os'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)