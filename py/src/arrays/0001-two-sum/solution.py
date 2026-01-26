def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for i, value in enumerate(nums):
        needed = target - value

        if needed in seen:
            return [seen[needed], i]

        seen[value] = i

    raise ValueError("No solution")
