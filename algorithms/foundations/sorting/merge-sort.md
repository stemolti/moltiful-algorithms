# Merge Sort

## Problem
Given a collection of elements, sort them in non-decreasing order.

Merge Sort is a **comparison-based, divide-and-conquer sorting algorithm**.

---

## High-level idea
The algorithm recursively divides the collection into two halves until subarrays
of size one are reached. These subarrays are then merged back together in sorted
order.

The key insight is that **merging two already sorted arrays can be done efficiently**.

---

## Algorithm steps
1. Divide the array into two halves.
2. Recursively apply Merge Sort to each half.
3. Merge the two sorted halves into a single sorted array.

---

## Correctness argument
Merge Sort is correct by induction on the size of the array.

**Base case:**  
An array of size 0 or 1 is trivially sorted.

**Inductive step:**  
Assume Merge Sort correctly sorts arrays of size less than `n`.  
For an array of size `n`, the algorithm:
- divides it into two smaller arrays,
- recursively sorts each one (by the inductive hypothesis),
- merges the two sorted arrays into a fully sorted array.

Since the merge step preserves order, the final array is sorted.

---

## Complexity
- **Time complexity:** `O(n log n)` in all cases
- **Space complexity:** `O(n)` due to auxiliary arrays

---

## Properties
- Stable: ✅
- In-place: ❌
- Comparison-based: ✅

---

## When to use
- When predictable performance is required
- When stability matters
- When working with linked lists or external sorting

---

## When NOT to use
- When memory usage must be minimal
- When in-place sorting is required

---

## Related concepts
- Divide and Conquer
- Recursion
- External sorting