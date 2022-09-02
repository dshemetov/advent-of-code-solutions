from advent2021.p18 import solve_a, solve_b, SnailfishTree

test_string = """"""


def test_example1():
    s = [
        """[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]""",
        """[[[[0,7],4],[7,[[8,4],9]]],[1,1]]""",
        """[[[[0,7],4],[15,[0,13]]],[1,1]]""",
        """[[[[0,7],4],[[7,8],[0,13]]],[1,1]]""",
        """[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]""",
        """[[[[0,7],4],[[7,8],[6,0]]],[8,1]]""",
    ]
    i = 0
    root_tree = SnailfishTree()
    root_tree.parse(eval(s[i]))
    root_tree.reduce()
    assert str(root_tree) == s[i + 1]
    i = 1
    root_tree = SnailfishTree()
    root_tree.parse(eval(s[i]))
    root_tree.reduce()

    assert str(root_tree) == s[i + 1]
    i = 2
    root_tree = SnailfishTree()
    root_tree.parse(eval(s[i]))
    root_tree.reduce()
    assert str(root_tree) == s[i + 1]
    i = 3
    root_tree = SnailfishTree()
    root_tree.parse(eval(s[i]))
    root_tree.reduce()
    assert str(root_tree) == s[i + 1]
    i = 4
    root_tree = SnailfishTree()
    root_tree.parse(eval(s[i]))
    root_tree.reduce()
    assert str(root_tree) == s[i + 1]

    s = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
    expected = """[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"""
    root_trees = []
    for line in s.split("\n"):
        st = SnailfishTree()
        st.parse(eval(line.strip()))
        root_trees += [st]

    end_tree = root_trees[0]
    for root_tree in root_trees[1:]:
        while end_tree.reduce():
            pass
        end_tree = end_tree + root_tree

    while end_tree.reduce():
        pass

    assert str(end_tree) == expected


def test_solve_a():
    assert solve_a(test_string) == 0


def test_solve_b():
    assert solve_b(test_string) == 0
