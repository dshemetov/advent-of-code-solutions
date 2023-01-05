# Advent of Code Solutions

[Advent of Code](https://adventofcode.com/) is a great set of Christmas-themed coding challenges.

## Usage

Requires Python >=3.9.

```sh
# Clone repo
git clone https://github.com/dshemetov/advent-of-code-solutions
cd advent-of-code-solutions

# Install (Python venv, dependencies)
make install

# Set AoC cookie in .env
make set-cookie

# Print the answer to puzzle 2021 day 2 part b
python runner.py solve -y 2021 -d 2 -p b

# Print the answer to current year's day 2 (both parts)
python runner.py solve -d 21

# Clear cached answer
python runner.py solve -y 2021 -d 2 -c

# See help for more
python runner.py solve --help
```

## Background

I first got into Advent of Code in December 2015, while spending time with the Sellin family in Los Angeles.
After a few days of doing not much more than playing SSX Tricky and drinking peppermint schnapps, my brain was beginning to decompress from a tough school semester.
Evin was toying with functional programming paradigms in JavaScript and I dabbled with Python.
Nerding out together on a very large couch, it was good times.

I periodically tinker with my old solutions and refactor them.
The old versions can be found in the commit log, though.
It's nice to look back and see yourself grow as a programmer.

- AoC 2021: 43/50 Python.
- AoC 2020: 32/50 Python.
- AoC 2019: ??/50 Mathematica.
- AoC 2018: 13/50 Mathematica. Lessons learned:
  - Mathematica has a some really cool builtin functions (e.g. see the three-line solution to Day 6 with [DistanceMatrix](https://reference.wolfram.com/language/ref/DistanceMatrix.html) and [Nearest](https://reference.wolfram.com/language/ref/Nearest.html)).
  - Even though Mathematica has fast built-ins, Python can be faster for simple for-loops (e.g. see Day 9 and the attached Python solution). I did not have the courage to try to implement a linked-list in Mathematica for Day 9.
  - Mathematica notebooks don't look great on GitHub.
  - Mathematica [doesn't support lazy iteration natively](https://mathematica.stackexchange.com/questions/226334/breaking-functional-loops-and-doing-lazy-evaluation-in-mathematica).
  - Mathematica doesn't make it easy to make new data structures (though [these are nice to have](https://reference.wolfram.com/language/guide/DataStructures.html)).
  - Mathematica debugging isn't easy (and it isn't easy to switch from developing code in a Notebook to Eclipse, where they maintain a debugger plugin).
- AoC 2015: ??/50 Python.
