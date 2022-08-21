import pytest
from .p18 import (
    evaluate_expression_a,
    evaluate_simple_expression_a,
    evaluate_expression_b,
    evaluate_simple_expression_b,
    evaluate_simple_additions,
)


def test_evaluate_simple_additions():
    assert evaluate_simple_additions("2 + 4 * 4 + 6") == "6 * 10"
    assert evaluate_simple_additions("13 + 5 * 4 + 6") == "18 * 10"
    assert evaluate_simple_additions("1 + 2 + 3 * 5") == "6 * 5"


def test_evaluate_simple_expression():
    assert evaluate_simple_expression_a("2 + 4 * 9") == "54"
    assert evaluate_simple_expression_a("((2 + 4 * 9))") == "54"
    assert evaluate_simple_expression_a("3 + 4 + 9 * 2") == "32"
    assert evaluate_simple_expression_b("2 + 4 * 9") == "54"
    assert evaluate_simple_expression_b("((2 + 4 * 9))") == "54"
    assert evaluate_simple_expression_b("3 + 4 + 9 * 2") == "32"
    assert evaluate_simple_expression_b("3 + 4 * 9 + 2") == "77"


def test_evaluate_expression():
    assert evaluate_expression_a("2 * 3 + (4 * 5)") == 26
    assert evaluate_expression_a("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert evaluate_expression_a("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert evaluate_expression_a("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
    assert evaluate_expression_b("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert evaluate_expression_b("2 * 3 + (4 * 5)") == 46
    assert evaluate_expression_b("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert evaluate_expression_b("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert evaluate_expression_b("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
    assert evaluate_expression_b("1 + 2") == 3
    assert evaluate_expression_b("1 + 2 + 3 + 4 + 5") == 15
    assert evaluate_expression_b("1 + 2 + 3 + 4 + 5 * 2") == 30
    assert evaluate_expression_b("5 * 6 * 2") == 60
    assert evaluate_expression_b("2 + 6 * (10)") == 80
    assert evaluate_expression_b("2 * 6 + (10)") == 32
    assert evaluate_expression_b("6 * 76 + 3 + 6912 * 9 + 6") == 629190
