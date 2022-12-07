from typer.testing import CliRunner

from runner import app

runner = CliRunner()


def test_app():
    runner.invoke(app, ["-d", 1])
