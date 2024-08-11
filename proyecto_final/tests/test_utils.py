import pytest

from ..utils import find_first

# Pruebas unitarias para la función find_first
def test_find_first_single_match():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]
    result = find_first(data, name='Bob')
    assert result == {'name': 'Bob', 'age': 25}

def test_find_first_no_match():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]
    result = find_first(data, name='Charlie')
    assert result == {}

def test_find_first_multiple_matches():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Alice', 'age': 35},
        {'name': 'Bob', 'age': 25}
    ]
    result = find_first(data, name='Alice')
    assert result == {'name': 'Alice', 'age': 30}

def test_find_first_with_multiple_conditions():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Alice', 'age': 35},
        {'name': 'Bob', 'age': 25}
    ]
    result = find_first(data, name='Alice', age=35)
    assert result == {'name': 'Alice', 'age': 35}

def test_find_first_empty_data():
    data = []
    result = find_first(data, name='Alice')
    assert result == {}

def test_find_first_empty_kwargs():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]
    result = find_first(data)
    assert result == {'name': 'Alice', 'age': 30}

def test_find_first_no_key_in_dict():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob'}
    ]
    result = find_first(data, age=30)
    assert result == {'name': 'Alice', 'age': 30}
