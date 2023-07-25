"""No Space Left On Device
https://adventofcode.com/2022/day/7
"""
import re


def print_dirs(dirs: dict, dir: str, indent: int = 0):
    print(" " * 2 * indent + " - " + dir)
    for child in dirs[dir]:
        if isinstance(child, str) and child.endswith("/"):
            print_dirs(dirs, child, indent + 1)
        else:
            print(" " * (2 * indent + 3) + child + " " + str(dirs[child]))


def get_dirs(s: str) -> dict:
    dir_to_subdir_map = {"/": []}
    cur_dir = "/"
    r = re.compile(r"(\d+) ([a-zA-Z0-9\.]+)")  # e.g. 14848514 b.txt

    for line in s.split("\n"):
        if not line:
            continue
        elif line.startswith("$ cd "):
            if line[5:] == "..":
                new_dir = cur_dir[: cur_dir[:-1].rfind("/") + 1]
            else:
                if line[5:] == "/":
                    new_dir = "/"
                else:
                    new_dir = cur_dir + line[5:] + "/"

            if new_dir not in dir_to_subdir_map:
                dir_to_subdir_map[cur_dir].append(new_dir)
                dir_to_subdir_map[new_dir] = []
            cur_dir = new_dir
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            new_dir = cur_dir + line[4:] + "/"
            if new_dir not in dir_to_subdir_map:
                dir_to_subdir_map[cur_dir].append(new_dir)
                dir_to_subdir_map[new_dir] = []
        else:
            num, name = r.findall(line)[0]
            dir_to_subdir_map[cur_dir].append(cur_dir + name)
            dir_to_subdir_map[cur_dir + name] = int(num)

    return dir_to_subdir_map


def get_dir_sizes(s: str) -> dict:
    dir_to_subdir_map = get_dirs(s)
    dir_sizes = {}

    def get_size(d: str) -> int:
        if d in dir_sizes:
            pass
        elif d.endswith("/"):
            dir_sizes[d] = sum(get_size(child) for child in dir_to_subdir_map[d])
        else:
            dir_sizes[d] = dir_to_subdir_map[d]
        return dir_sizes[d]

    get_size("/")
    return dir_sizes


def solve_a(s: str) -> int:
    """
    Examples:
    >>> solve_a(test_string)
    95437
    """
    s = s.strip("\n")
    dir_sizes = get_dir_sizes(s)
    return sum(
        size for key, size in dir_sizes.items() if key.endswith("/") and size <= 100000
    )


def solve_b(s: str) -> int:
    """
    Examples:
    >>> solve_b(test_string)
    24933642
    """
    s = s.strip("\n")
    dir_sizes = get_dir_sizes(s)
    space_needed = 30_000_000 - (70_000_000 - dir_sizes["/"])
    return min(
        size
        for key, size in dir_sizes.items()
        if key.endswith("/") and size >= space_needed
    )


test_string = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
