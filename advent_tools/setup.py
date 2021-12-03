from setuptools import setup
from setuptools import find_packages

from os import mkdir, environ
from os.path import exists, join

required = [
    "python-dotenv",
    "joblib",
    "requests"
]

home_dir = environ["HOME"]

if not exists(join(home_dir, ".advent_tools")):
    mkdir(join(home_dir, ".advent_tools"))

if not exists(join(home_dir, ".advent_tools/joblib_cache")):
    mkdir(join(home_dir, ".advent_tools/joblib_cache"))

setup(
    name="advent_tools",
    version="0.1.0",
    description="Utilities for Advent of Code Puzzles",
    author="Dmitry Shemetov",
    url="https://github.com/dshemetov/",
    install_requires=required,
    classifiers=[
        "Development Status :: 4 - Working Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9.7",
    ],
    packages=find_packages()
)
