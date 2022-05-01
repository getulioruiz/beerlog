from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )
    assert result.exit_code == 0
    assert "Beer added" in result.stdout


def test_list_beers():
    result = runner.invoke(main, ["list"])
    assert result.exit_code == 0
    assert "Beerlog Database" in result.stdout


def test_list_beer_with_specific_style():
    test_add_beer()
    result = runner.invoke(main, ["list", "--style=KornPA"])
    assert result.exit_code == 0
    assert "Beerlog KornPA" in result.stdout
