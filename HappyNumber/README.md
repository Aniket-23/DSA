# Happy Number

## Problem Description

A **happy number** is defined using the following process:

1. Start with any positive integer `n`.
2. Replace the number by the sum of the squares of its digits.
3. Repeat this process until:
   - The number becomes `1`, meaning it is a **happy number**.
   - It falls into a cycle that **does not include 1**, meaning it is **not a happy number**.
4. Return `true` if `n` is a happy number, otherwise return `false`.

---

## Examples

### Example 1:
**Input**:  
`n = 19`  

**Output**:  
`true`  

**Explanation**:  
- \(1^2 + 9^2 = 1 + 81 = 82\)
- \(8^2 + 2^2 = 64 + 4 = 68\)
- \(6^2 + 8^2 = 36 + 64 = 100\)
- \(1^2 + 0^2 + 0^2 = 1\)  
- Since we reached `1`, `19` is a happy number.

---

### Example 2:
**Input**:  
`n = 2`  

**Output**:  
`false`  

**Explanation**:  
- \(2^2 = 4\)
- \(4^2 = 16\)
- \(1^2 + 6^2 = 1 + 36 = 37\)
- \(3^2 + 7^2 = 9 + 49 = 58\)
- \(5^2 + 8^2 = 25 + 64 = 89\)
- \(8^2 + 9^2 = 64 + 81 = 145\)
- \(1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42\)
- \(4^2 + 2^2 = 16 + 4 = 20\)
- \(2^2 + 0^2 = 4\) (cycle repeats)

Since `n` falls into a cycle that **does not include 1**, `2` is **not** a happy number.

---

## Constraints

- \(1 \leq n \leq 2^{31} - 1\)

---

## Algorithm

1. **Create a function to compute the sum of squares of digits**:
   - Extract each digit of `n`.
   - Compute the square of each digit and sum them.
   
2. **Use a loop to iterate the process**:
   - If `n` becomes `1`, return `true`.
   - Keep track of previously seen numbers in a set to detect cycles.
   - If a number repeats, return `false`.

---

## Complexity

- **Time Complexity**:  
  - \(O(\log n)\) per iteration since we process the digits of `n`.
  - The process typically terminates quickly due to number reduction.

- **Space Complexity**:  
  - \(O(\log n)\) for storing numbers in the set (for cycle detection).
