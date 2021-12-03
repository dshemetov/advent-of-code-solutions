import pytest
from .p18b import evaluate_simple_expression, evaluate_expression, evaluate_simple_additions

class TestExpr:
    def test_evaluate_simple_additions(self):
        assert evaluate_simple_additions("2 + 4 * 4 + 6") == "6 * 10"
        assert evaluate_simple_additions("13 + 5 * 4 + 6") == "18 * 10"
        assert evaluate_simple_additions("1 + 2 + 3 * 5") == "6 * 5"

    def test_evaluate_simple_expression(self):
        assert evaluate_simple_expression("2 + 4 * 9") == "54"
        assert evaluate_simple_expression("((2 + 4 * 9))") == "54"
        assert evaluate_simple_expression("3 + 4 + 9 * 2") == "32"
        assert evaluate_simple_expression("3 + 4 * 9 + 2") == "77"

    def test_evaluate_expression(expr: str) -> int:
        assert evaluate_expression("1 + (2 * 3) + (4 * (5 + 6))") ==  51
        assert evaluate_expression("2 * 3 + (4 * 5)") ==  46
        assert evaluate_expression("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
        assert evaluate_expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
        assert evaluate_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
        assert evaluate_expression("1 + 2") == 3
        assert evaluate_expression("1 + 2 + 3 + 4 + 5") == 15
        assert evaluate_expression("1 + 2 + 3 + 4 + 5 * 2") == 30
        assert evaluate_expression("5 * 6 * 2") == 60
        assert evaluate_expression("2 + 6 * (10)") == 80
        assert evaluate_expression("2 * 6 + (10)") == 32
        assert evaluate_expression("6 * 76 + 3 + 6912 * 9 + 6") == 629190
