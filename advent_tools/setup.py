from setuptools import setup
from setuptools import find_packages

required = [
    "joblib",
    "more-itertools",
    "numpy",
    "python-dotenv",
    "requests"
]

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
        "Programming Language :: Python :: 3.10.5",
    ],
    packages=find_packages()
)
