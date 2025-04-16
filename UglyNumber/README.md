# Ugly Number Checker

## Problem Statement
An **ugly number** is a positive integer that has no prime factors other than `2`, `3`, and `5`. Given an integer `n`, return `True` if `n` is an ugly number; otherwise, return `False`.

## Examples

### Example
**Input:**  
n = 6

**Output:**  
True

**Explanation:**  
6 can be factorized as `2 × 3`, and since all prime factors belong to `{2, 3, 5}`, it is an **ugly number**.

**Explanation:**  
14 can be factorized as `2 × 7`, but **7 is not in {2, 3, 5}**, so it is **not an ugly number**.

## Constraints
- `-2^31 ≤ n ≤ 2^31 - 1`
- Ugly numbers must be **positive integers**.

## Approach
To determine if a number is ugly:
1. **Keep dividing** `n` by `2`, `3`, and `5` while it remains divisible.
2. **If the final result is 1**, `n` is ugly.
3. **If there's any leftover prime factor (like 7, 11, etc.), it's not ugly.**