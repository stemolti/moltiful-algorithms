# Definition of Done (DoD)

This document defines the criteria that must be satisfied before an algorithmic
problem is considered complete inside the `moltiful-algorithms` repository.

The goal is to enforce consistency, correctness, clarity, and long-term maintainability.
A problem is not considered done simply because it passes tests.

---

## 1. Structural Requirements

A problem is considered structurally complete when:

- [ ] The folder follows the canonical naming convention: `NNNN-slug`
- [ ] A `README.md` file exists inside the problem folder
- [ ] `solution.ts` or `solution.py` (or both) exists
- [ ] Corresponding test file exists (`solution.test.ts` / `test_solution.py`)
- [ ] Tests pass locally
- [ ] CI pipeline passes successfully

If any of the above is missing, the problem is not complete.

---

## 2. Correctness & Analysis

The solution must demonstrate formal understanding, not just functional output.

- [ ] Brute-force approach is understood (even if not implemented)
- [ ] Final approach is clearly documented
- [ ] A correctness argument is written
- [ ] Time complexity is derived and explicitly stated
- [ ] Space complexity is derived and explicitly stated
- [ ] Relevant edge cases are explicitly listed

The correctness argument must explain *why* the solution works,
not merely describe what it does.

---

## 3. Code Quality Standards

The implementation must meet basic engineering standards:

- [ ] Clear and meaningful variable naming
- [ ] No unnecessary variables or redundant logic
- [ ] No hidden side effects unless intentional
- [ ] No magic numbers without explanation
- [ ] Handles empty input (if applicable)
- [ ] Handles minimal valid input
- [ ] Handles duplicates and negative values (if applicable)

Readable and predictable code is preferred over clever but opaque solutions.

---

## 4. Conceptual Integration

Each problem must be integrated into the broader knowledge structure of the repository.

- [ ] Problem is categorized correctly (e.g., `arrays/`, `graphs/`, `dp/`)
- [ ] Related foundations are referenced
- [ ] No duplicated theoretical explanations across files
- [ ] Reusable patterns are linked instead of rewritten
