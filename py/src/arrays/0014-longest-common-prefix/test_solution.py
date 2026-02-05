import pytest
from solution import two_sum


def test_returns_indices_of_two_numbers_that_sum_to_target():
    nums = [2, 7, 11, 15]
    target = 9

    result = two_sum(nums, target)

    assert result == [0, 1]


def test_works_with_negative_numbers():
    nums = [-3, 4, 3, 90]
    target = 0

    result = two_sum(nums, target)

    assert result == [0, 2]


def test_does_not_reuse_the_same_element_twice():
    nums = [3, 3]
    target = 6

    result = two_sum(nums, target)

    assert result == [0, 1]


def test_raises_error_when_no_solution_exists():
    nums = [1, 2, 3]
    target = 7

    with pytest.raises(ValueError, match="No solution"):
        two_sum(nums, target)
