#!/usr/bin/env python
from codecs import open
from os import path

from setuptools import setup, find_packages


def read(*names, **kwargs):
    with open(
            path.join(path.dirname(__file__), *names),
            encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


CURRENT_VERSION = '0.2.2-post3'

setup(
    name='pysvg-py3',
    version=CURRENT_VERSION,
    description='Python 3 portage of pysvg',
    long_description=read('README.md'),
    author='Kerim Mansour',
    author_email='',
    url='https://github.com/alorence/pysvg-py3',
    packages=find_packages(),
    # Files included in sdist (using MANIFEST.in) will also be included in bdist*
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia :: Graphics",
    ]
)
