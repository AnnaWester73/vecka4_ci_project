import pytest
from src.names import create_name_list, name_exists


@pytest.mark.integration
def test_name_exists_uses_created_name_list():
    names = create_name_list()

    assert "Anna" in names
    assert name_exists("Anna") is True


@pytest.mark.integration
def test_name_exists_returns_false_if_not_in_created_list():
    names = create_name_list()

    assert "Sessan" not in names
    assert name_exists("Sessan") is False
