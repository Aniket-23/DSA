# Find the Square Root (Rounded Down) of a Non-Negative Integer

## Problem Description

Given a non-negative integer `x`, the task is to calculate the square root of `x` rounded down to the nearest integer. The result must also be a non-negative integer.

**Note**:  
You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` in C++ or `x ** 0.5` in Python.

---

## Examples

### Example 1
**Input**:  
`x = 4`  

**Output**:  
`2`  

**Explanation**:  
The square root of `4` is `2`.  

---

### Example 2
**Input**:  
`x = 8`  

**Output**:  
`2`  

**Explanation**:  
The square root of `8` is approximately `2.82842`. Rounded down to the nearest integer, the result is `2`.

---

## Constraints

- \(0 \leq x \leq 2^{31} - 1\)

---

## Algorithm

1. **Define the Search Space**:  
   - Use a binary search approach where the search space is defined between `0` and `x`. For numbers less than `2`, return `x` directly since their square root rounded down is the number itself.

2. **Binary Search**:
   - Compute the middle point, `mid`, of the current search space.
   - Calculate `mid * mid`:
     - If `mid * mid` equals `x`, return `mid` as it is the exact square root.
     - If `mid * mid` is less than `x`, move the left boundary of the search space to `mid + 1`, as the square root must be larger.
     - If `mid * mid` is greater than `x`, move the right boundary of the search space to `mid - 1`, as the square root must be smaller.

3. **Return the Result**:
   - The loop continues until the search space is exhausted.
   - The right boundary (`right`) will contain the largest integer whose square is less than or equal to `x`.

---

## Complexity

- **Time Complexity**:  
  \(O(\log(x))\), as the binary search reduces the search space by half at each step.

- **Space Complexity**:  
  \(O(1)\), since no extra space is used apart from a few variables.

---

## Example Execution

### Input: `x = 8`

1. Initial range: `left = 0`, `right = 8`.
2. Compute `mid = (0 + 8) // 2 = 4`.  
   - \(4^2 = 16\), which is greater than `8`. Update `right = 3`.
3. Compute `mid = (0 + 3) // 2 = 1`.  
   - \(1^2 = 1\), which is less than `8`. Update `left = 2`.
4. Compute `mid = (2 + 3) // 2 = 2`.  
   - \(2^2 = 4\), which is less than `8`. Update `left = 3`.
5. Compute `mid = (3 + 3) // 2 = 3`.  
   - \(3^2 = 9\), which is greater than `8`. Update `right = 2`.
6. Loop terminates, and `right = 2` is the answer.

**Output**: `2`
