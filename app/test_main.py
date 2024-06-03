import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
        (50, [0, 0, 0, 2]),
        (17, [2, 1, 1, 0])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    result = get_coin_combination(cents)
    assert result == expected, (
        f"For {cents} cents, expected {expected} but got {result}"
    )
