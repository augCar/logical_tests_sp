import pytest
from src.fizz_buzz import fizz_buzz


@pytest.mark.parametrize(
    ['input', 'output'],
    [
        (1, "\n1\n\n"),
        (2, "\n1\n2\n\n"),
        (3, "\n1\n2\nFizz\n\n"),
        (4, "\n1\n2\nFizz\n4\n\n"),
        (5, "\n1\n2\nFizz\n4\nBuzz\n\n"),
        (6, "\n1\n2\nFizz\n4\nBuzz\nFizz\n\n"),
        (7, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n\n"),
        (8, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\n\n"),
        (9, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\n\n"),
        (10, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n\n"),
        (11, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\n\n"),
        (12, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n\n"),
        (13, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n\n"),
        (14, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\n\n"),
        (15, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n\n"),
        (16, "\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n\n")
    ]
)
def test_fizz_buzz(capsys, input, output):
    fizz_buzz(input)
    captured = capsys.readouterr()
    assert captured.out == output
