# Power of Two

## Problem Statement

Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two if there exists an integer `x` such that:

n == 2^x

## Algorithm (Iterative Division Approach)

1. If `n` is `0`, return `false` since 0 is not a power of two.
2. While `n` is greater than 0:
   - If `n` becomes `1`, return `true`.
   - If `n` is not divisible by `2`, break the loop and return `false`.
   - Otherwise, divide `n` by `2` (integer division).
3. If loop completes without reaching `1`, return `false`.

---

## Time and Space Complexity

- **Time Complexity:** O(log n)  
  The number is divided by 2 each iteration until it reaches 1.

- **Space Complexity:** O(1)  
  Uses a constant amount of space.

---