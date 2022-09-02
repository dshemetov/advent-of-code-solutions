from advent2021.p16 import hex_to_bin, read_binary, read_packet_header, solve_a, solve_b

test_strings = [
    """D2FE28""",
]


def test_solve_a():
    # assert solve_a(test_string) == 0
    assert hex_to_bin(test_strings[0]) == [int(x) for x in "110100101111111000101000"]
    assert read_packet_header(hex_to_bin(test_strings[0])) == (6, 4)
    assert read_binary(hex_to_bin(test_strings[0])) == ([6], [2021])


def test_solve_b():
    assert solve_b(test_strings[0]) == 0
