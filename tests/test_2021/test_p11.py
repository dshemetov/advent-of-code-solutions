from advent2021.p11 import np, parse_input, run_octopus_step, run_octopus_steps, solve_a, solve_b

test_string_10 = [
    """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""",
    """0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000""",
    """3936556452
5686556806
4496555690
4448655580
4456865570
5680086577
7000009896
0000000344
6000000364
4600009543""",
    """0643334118
4253334611
3374333458
2225333337
2229333338
2276733333
2754574565
5544458511
9444447111
7944446119""",
    """0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766""",
]

test_string_5 = [
    """11111
19991
19191
19991
11111""",
    """34543
40004
50005
40004
34543""",
    """45654
51115
61116
51115
45654""",
]


def test_solve_a():
    mat0 = parse_input(test_string_5[0])
    out_mat, out_flashes = run_octopus_step(mat0)
    expected_mat = parse_input(test_string_5[1])
    np.testing.assert_allclose(out_mat, expected_mat)
    assert out_flashes == 9
    out_mat, out_flashes = run_octopus_step(out_mat)
    expected_mat = parse_input(test_string_5[2])
    np.testing.assert_allclose(out_mat, expected_mat)
    assert out_flashes == len(expected_mat[np.where(expected_mat == 0)])

    mat0 = parse_input(test_string_10[0])
    _, out_flashes = run_octopus_steps(mat0, 10)
    expected_mat = parse_input(test_string_10[1])
    assert out_flashes == 204

    mat0 = parse_input(test_string_10[0])
    out_mat, out_flashes = run_octopus_steps(mat0, 20)
    expected_mat = parse_input(test_string_10[2])
    np.testing.assert_allclose(out_mat, expected_mat)

    mat0 = parse_input(test_string_10[0])
    out_mat, out_flashes = run_octopus_steps(mat0, 30)
    expected_mat = parse_input(test_string_10[3])
    np.testing.assert_allclose(out_mat, expected_mat)

    mat0 = parse_input(test_string_10[0])
    out_mat, out_flashes = run_octopus_steps(mat0, 100)
    expected_mat = parse_input(test_string_10[4])
    np.testing.assert_allclose(out_mat, expected_mat)

    assert solve_a(test_string_10[0]) == 1656


def test_solve_b():
    assert solve_b(test_string_10[0]) == 195
