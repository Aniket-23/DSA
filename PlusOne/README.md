# Increment a Large Integer Represented as an Array

## Problem Description

You are given a large integer represented as an array of digits, where each `digits[i]` is the \(i^{th}\) digit of the integer. The digits are ordered from **most significant** to **least significant** in left-to-right order. The integer does not contain any leading zeros.

The task is to increment the large integer by **1** and return the resulting array of digits.

---

## Examples

### Example 1:
**Input**:  
`digits = [1, 2, 3]`  

**Output**:  
`[1, 2, 4]`  

**Explanation**:  
The array represents the integer `123`. Incrementing by one gives `123 + 1 = 124`.  

---

### Example 2:
**Input**:  
`digits = [4, 3, 2, 1]`  

**Output**:  
`[4, 3, 2, 2]`  

**Explanation**:  
The array represents the integer `4321`. Incrementing by one gives `4321 + 1 = 4322`.

---

### Example 3:
**Input**:  
`digits = [9]`  

**Output**:  
`[1, 0]`  

**Explanation**:  
The array represents the integer `9`. Incrementing by one gives `9 + 1 = 10`.  

---

## Constraints

- \(1 \leq \text{digits.length} \leq 100\)
- \(0 \leq \text{digits}[i] \leq 9\)
- The input array does not contain any leading zeros.

---

## Algorithm

1. **Initialize Carry**:
   - Start with `carry = 1` since the task is to increment the integer by `1`.

2. **Traverse the Array from Right to Left**:
   - Start iterating from the last digit (least significant digit) to the first digit (most significant digit).

3. **Update Each Digit**:
   - Add the `carry` to the current digit.
   - If the resulting value is less than `10`, update the digit with the new value, set `carry = 0`, and terminate the loop as no further propagation is needed.
   - If the resulting value is `10`, set the current digit to `0` and continue propagating the carry to the next digit.

4. **Handle Remaining Carry**:
   - After completing the loop, if there is still a carry (e.g., in cases like `[9, 9, 9]`), prepend `1` to the array.

5. **Return the Result**:
   - The modified array represents the incremented number.

---

### Example Execution for Input `digits = [9, 9, 9]`:

1. Start with `carry = 1`.
2. Traverse from right to left:
   - Add `1` to `9` → Result: `10`. Set digit to `0`, propagate `carry = 1`.
   - Add `1` to the next `9` → Result: `10`. Set digit to `0`, propagate `carry = 1`.
   - Add `1` to the next `9` → Result: `10`. Set digit to `0`, propagate `carry = 1`.
3. At the end of the array, `carry = 1`. Prepend `1` to the array.
4. Result: `[1, 0, 0, 0]`.

---

## Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the array, since we traverse the array at most once.
- **Space Complexity**: \(O(1)\), as the operation modifies the input array in place, except when a new digit is added at the start.
