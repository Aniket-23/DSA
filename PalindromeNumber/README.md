# Palindrome Number

## Problem Description

Given an integer `x`, determine whether it is a palindrome. A palindrome is a number that reads the same backward as forward.

### Examples:

#### Example 1:
- **Input:** `x = 121`
- **Output:** `true`
- **Explanation:** `121` reads as `121` from left to right and from right to left.

#### Example 2:
- **Input:** `x = -121`
- **Output:** `false`
- **Explanation:** From left to right, it reads `-121`. From right to left, it becomes `121-`, which is not a palindrome.

#### Example 3:
- **Input:** `x = 10`
- **Output:** `false`
- **Explanation:** Reads `01` from right to left, which is not the same as `10`.

---

## Constraints
- The integer `x` can be any 32-bit signed integer.

---

## Solution

### Algorithm:
1. Convert the integer to a string.
2. Compare the string with its reverse:
   - If they are the same, return `true`.
   - Otherwise, return `false`.
3. Handle edge cases such as negative numbers, which cannot be palindromes.

---

