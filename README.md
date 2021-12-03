# Advent of Code Solutions

[Advent of Code](https://adventofcode.com/) is a great set of Christmas-themed puzzles.

To setup:

```sh
# Install my tools package (puzzle input fetching and caching utility)
pip install -e advent_tools

# Get your AoC cookie (login on Advent of Code and inspect your browser session)
echo "AOC_TOKEN=your_cookie" > ~/.advent_tools/.env
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

## AoC 2021

Python forever.

## AoC 2020

Back to Python!

## AoC 2019

Still in a Mathematica Phase.

## AoC 2018

This year I got through about 13 problems in the set.
I had a lot of fun learning functional programming with Mathematica's training wheels and finding compact (and sometimes not) ways to solve problems.
Problems with more complex data structures and non-array logic were a lot harder to write and debug.

Things learned:
* Mathematica has a built-in function for almost everything (e.g. see the three-line solution to Day 6 with [DistanceMatrix](https://reference.wolfram.com/language/ref/DistanceMatrix.html) and [Nearest](https://reference.wolfram.com/language/ref/Nearest.html)).
* Even though Mathematica has fast built-ins, Python can be faster for simple for-loops (e.g. see Day 9 and the attached Python solution). I did not have the courage to try to implement a linked-list in Mathematica for Day 9.

If only Mathematica notebooks were GitHub viewable.

## AoC 2015

I got into these puzzles in December 2015 in Los Angeles, while spending time with the Sellin family.
After a few days of doing not much more than playing SSX Tricky and drinking peppermint schnapps, our brains started to come alive again.
Evin Sellin was really enjoying functional programming paradigms in JavaScript.
There was a very large couch.
It was a very nice time.

I'm going to update these solutions, but you can look at the old versions for fun here.
It feels nice to look back and see your own growth as a programmer.
