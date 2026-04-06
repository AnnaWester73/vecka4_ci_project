import pytest
from src.names import name_exists, create_name_list


@pytest.mark.unit
def test_create_name_list_is_not_empty():
    names = create_name_list()
    assert len(names) > 0


@pytest.mark.unit
def test_name_exists_returns_true_for_existing_name():
    assert name_exists("Anna") is True


@pytest.mark.unit
def test_name_exists_returns_false_for_missing_name():
    assert name_exists("Sessan") is False
