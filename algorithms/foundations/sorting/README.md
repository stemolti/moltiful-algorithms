# Sorting Algorithms

## Overview
Sorting algorithms reorder elements of a collection according to a defined order
(e.g. ascending or descending). They are fundamental building blocks used in
searching, optimization, and data processing.

Different sorting algorithms make different trade-offs in terms of:
- time complexity
- space usage
- stability
- adaptability to input characteristics

---

## Classification

### Comparison-based
- Merge Sort
- Quick Sort
- Heap Sort

### Non-comparison-based
- Counting Sort
- Radix Sort
- Bucket Sort

---

## When to use which

| Algorithm      | Time (avg) | Space | Stable | Notes |
|---------------|-----------|-------|--------|------|
| Merge Sort    | O(n log n) | O(n)  | Yes    | Predictable, good for linked lists |
| Quick Sort    | O(n log n) | O(log n) | No | Fast in practice, bad worst-case |
| Heap Sort     | O(n log n) | O(1)  | No     | In-place, not stable |
| Counting Sort | O(n + k)   | O(k)  | Yes    | Only for small integer ranges |

---

## Related techniques
- Divide and Conquer
- Heap data structure
