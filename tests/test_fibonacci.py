import pytest
from src.fibonacci import calculate_fibonacci

@pytest.mark.parametrize(
    ['secuence_length', 'output'],
    [
        (2, [0, 1]),
        (3, [0, 1, 1])
    ]
)
def test_suma(secuence_length, output): # there's a failure in the base case with input 1
    assert calculate_fibonacci(secuence_length) == output

"""
[
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (4, [0, 1, 1, 2]),
    (5, [0, 1, 1, 2, 3]),
    (6, [0, 1, 1, 2, 3, 5]),
    (7, [0, 1, 1, 2, 3, 5, 8]),
    (8, [0, 1, 1, 2, 3, 5, 8, 13]),
    (9, [0, 1, 1, 2, 3, 5, 8, 13, 21]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
]
"""