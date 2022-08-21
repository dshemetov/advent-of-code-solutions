# Advent of Code Solutions

[Advent of Code](https://adventofcode.com/) is a great set of Christmas-themed puzzles.

To setup, use Python 3.9+, and:

```sh
# Clone repo
git clone https://github.com/dshemetov/advent-of-code-solutions
cd advent-of-code-solutions

# Install (Python dependencies, asks for AoC cookie)
make install
```

The problem runner can be used as follows:

```sh
# Print the answer to 2021 puzzle day 2 part b
python runner.py -s 2021.2.b
```

The runner caches results by default, you can clear the answer cache and rerun with the `-c` flag:

```sh
# Clear answer cache
python runner.py -s 2021.2.b -c
```

Test and format (with black)

```sh
make test

make format
```

## Background

I got into these puzzles in December 2015 in Los Angeles, while spending time with the Sellin family.
After a few days of doing not much more than playing SSX Tricky and drinking peppermint schnapps, my brain was beginning to decompress from a tough school semester.
Evin was toying functional programming paradigms in JavaScript and I dabbled with Python.
Together on a very large couch, it was a very nice time.

I'm going to update these solutions at some point, but you can look at the old versions for fun here.
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
