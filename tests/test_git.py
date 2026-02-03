import pytest
from gjira.git import get_branch_name, get_branch_id, validate_branch_name


def test_get_branch_name(mocker, git_branch):
    mock = git_branch()
    get_branch_name()
    mock.assert_called_once_with(("git", "rev-parse", "--abbrev-ref", "HEAD"))


def test_get_branch_id(mocker, git_branch):
    mock = git_branch("JIRA-1234_test-one-two")

    id = get_branch_id(r"JIRA-\d+")

    assert id == "JIRA-1234"
    mock.assert_called_once()


def test_get_branch_id_invalid(mocker, git_branch):
    git_branch("invalid-branch")

    with pytest.raises(SystemExit) as exc_info:
        get_branch_id(r"JIRA-\d+")
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0


def test_validate_branch_name():
    assert validate_branch_name(
        "JIRA-1234_hello-world", r"JIRA-\d+_[a-z]+(-[a-z]+)*$"
    ) == ["-world"]


def test_validate_branch_name_with_invalid_branch():
    assert validate_branch_name("JIRAhello-world", r"JIRA-\d+_[a-z]+(-[a-z]+)*$") == None
