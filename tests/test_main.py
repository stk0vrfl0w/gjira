import pytest
from gjira.__main__ import main
from gjira.commands import cli


def test_main(mocker):
    # Mock sys.argv to provide help command which exits with 0
    mocker.patch("sys.argv", ["gjira", "--help"])
    
    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0


def test_cli_has_commands():
    # Test that both commands are registered with the CLI group
    command_names = [cmd.name for cmd in cli.commands.values()]
    assert "append-jira" in command_names
    assert "check-branch" in command_names
