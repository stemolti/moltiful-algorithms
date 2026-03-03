# Moltiful Algorithms & Data Structures

> “Move slowly if you must - clarity first, speed will follow.<br>
> Do not chase solutions, but build the mind that can generate them.  
> Discipline's the key - structure over chaos, depth over noise.”

## Philosophy

This repository is designed to train **deep algorithmic reasoning**, not shallow pattern memorization.

The goal is to reach a level where:

- You can derive solutions under pressure.
- You can explain invariants clearly.
- You can reason about trade-offs.
- You can defend complexity analysis rigorously.
- You can write production-grade, review-ready code.

This is not a LeetCode dump.  
This is a **systematic, multi-language DSA mastery repository**.

## Core Principles

- **Reasoning first**  
  Every solution must explain _why_ it works.

- **Invariants > Tricks**  
  Identify what remains true at each step.

- **Trade-off awareness**  
  Compare brute force vs optimized vs alternative approaches.

- **Complexity explicitness**  
  Time and space complexity must be justified.

- **Edge case discipline**  
  Empty input, single element, duplicates, overflow, boundaries.

- **Clean code standard**  
  Clear naming, minimal cleverness, maintainable structure.

## Rrepository Structure

```
moltiful-algorithms/
│
├─ algorithms/
│  ├─ arrays/
│  ├─ dp/
│  ├─ foundations/
│  │  ├─ data-structures/
│  │  ├─ graph-traversal/
│  │  ├─ searching/
│  │  ├─ sorting/
│  │  └─ tecniques/
│  └─ graphs/
│
├─ docs/
│  └─ process/
│     ├─ ...
│     ├─ definition-of-done.md
│     └─ definition-of-learnt.md
│
├─ leetcode/
│  ├─ arrays/
│  │  ├─ 0001-two-sum.md
│  │  └─ ...
│  └─ ...
│
├─ packages/
│  ├─ js/
│  └─ ts/
│
├─ py/
│
├─ ...
├─ package.json
├─ pnpm-workspace.yaml
└─ README.md
```

This is a monorepo, packages-first, test-driven.

## Quality Gates

Two explicit standards define completion:

### Definition of Done

A solution is considered “done” only if:

- Tests pass
- Edge cases covered
- Complexity explained
- Code readable
- Invariant stated

### Definition of Learnt

A problem is considered “learnt” only if:

- The core pattern is extracted
- The invariant is internalized
- Failure modes are understood
- The solution can be re-derived without looking

## Data Structures

- [Stack](algorithms/foundations/data-structures/stack.md)

## Algorithms

- **Sorting**
  - [Merge Sort](algorithms/foundations/sorting/merge-sort.md)

## How to use this repository

**Requirements**

- Node 20+
- pnpm 9+
- Python 3.10+

**Install all dependencies**

```
pnpm install
```

**Run lint**

You may want to run it to check code quality.

```
pnpm lint
```

**Run all tests**

```
pnpm test
```

**Run tests for specific package**

```
pnpm -C packages/ts test
pnpm -C packages/js test
pnpm -C packages/py test
```

## Author

[@stemolti](https://stemolti.com)
