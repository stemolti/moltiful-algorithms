export function twoSum(nums: number[], target: number): [number, number] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const needed = target - nums[i]!;
    const index = seen.get(needed);

    if (index !== undefined) {
      return [index, i];
    }

    seen.set(nums[i]!, i);
  }

  throw new Error("No solution");
}
