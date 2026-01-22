import { describe, it, expect } from "vitest";
import { twoSum } from "./twoSum";

describe("twoSum", () => {
  it("returns indices of two numbers that sum to target", () => {
    const nums = [2, 7, 11, 15];
    const target = 9;

    const result = twoSum(nums, target);

    expect(result).toEqual([0, 1]);
  });

  it("works with negative numbers", () => {
    const nums = [-3, 4, 3, 90];
    const target = 0;

    const result = twoSum(nums, target);

    expect(result).toEqual([0, 2]);
  });

  it("does not reuse the same element twice", () => {
    const nums = [3, 3];
    const target = 6;

    const result = twoSum(nums, target);

    expect(result).toEqual([0, 1]);
  });

  it("throws an error when no solution exists", () => {
    const nums = [1, 2, 3];
    const target = 7;

    expect(() => twoSum(nums, target)).toThrow("No solution");
  });
});
