from typer.testing import CliRunner

from run import app

runner = CliRunner()


def test_app():
    runner.invoke(app, ["solve", "-y", 2022, "-d", 11, "-c"])
