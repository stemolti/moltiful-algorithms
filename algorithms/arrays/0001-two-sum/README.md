# 0001 — Two Sum

## Problem
Given a collection of integers and a target integer, determine whether there exist **two distinct elements** in the collection whose sum is equal to the target.  
If such a pair exists, return their indices. Each element may be used **at most once**.

The problem guarantees that **exactly one valid solution exists**.

---

## Approach
Scan the collection from left to right while maintaining a hash-based lookup structure that maps previously seen values to their indices.

For each element at index `i`:
1. Compute the complement needed to reach the target (`target - current_value`).
2. Check whether this complement has already been seen.
   - If yes, return the index of the complement and the current index.
3. Otherwise, store the current value and its index in the lookup structure.

This approach ensures that each element is processed once and that the pair, when found, uses two distinct indices.

---

## Correctness argument
We prove that the algorithm returns a correct pair of indices.

At any iteration `i`, the lookup structure contains exactly the values from indices `0` to `i - 1`.  
If a valid solution uses index `i` as the second element, then the first element must be the complement `target - nums[i]`, and its index must be less than `i`.

The algorithm explicitly checks whether this complement exists in the lookup structure before inserting the current element.  
When the complement is found, the algorithm returns the corresponding index pair, which sums to the target and consists of two distinct elements.

Since the problem guarantees the existence of exactly one solution, the first pair found by this process is necessarily the correct one.

---

## Complexity
- **Time complexity:** `O(n)`, where `n` is the number of elements in the collection.  
  Each element is processed once, and hash table operations are constant time on average.
- **Space complexity:** `O(n)` for storing previously seen elements in the lookup structure.

---

## Edge cases
- Duplicate values in the input (e.g. `[3, 3]` with target `6`), ensuring the same element is not reused.
- Negative numbers and mixed positive/negative values.
- Minimal input size where only one valid pair exists.
- Order of indices matters only in terms of distinctness, not relative position.
