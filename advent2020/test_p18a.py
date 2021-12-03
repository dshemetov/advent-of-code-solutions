import pytest
from .p18a import evaluate_expression, evaluate_simple_expression

class TestExpr:
    def test_evaluate_simple_expression(self):
        assert evaluate_simple_expression("2 + 4 * 9") == "54"
        assert evaluate_simple_expression("((2 + 4 * 9))") == "54"
        assert evaluate_simple_expression("3 + 4 + 9 * 2") == "32"

    def test_evaluate_expression(expr: str) -> int:
        assert evaluate_expression("2 * 3 + (4 * 5)") ==  26
        assert evaluate_expression("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
        assert evaluate_expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
        assert evaluate_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
