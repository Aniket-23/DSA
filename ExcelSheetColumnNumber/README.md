# Excel Sheet Column Number

## Problem Description

Given a string `columnTitle` that represents a column title as it appears in an Excel sheet, the task is to return its corresponding column number.

### Excel Column Mapping:

- **A** -> 1  
- **B** -> 2  
- **C** -> 3  
- ...  
- **Z** -> 26  
- **AA** -> 27  
- **AB** -> 28  
- ...  

This follows a pattern similar to base-26 numbering, where each letter represents a digit in the system.

---

## Examples

### Example 1:
**Input**:  
`columnTitle = "A"`  

**Output**:  
`1`  

---

### Example 2:
**Input**:  
`columnTitle = "AB"`  

**Output**:  
`28`  

---

### Example 3:
**Input**:  
`columnTitle = "ZY"`  

**Output**:  
`701`  

---

## Constraints

- \(1 \leq \text{columnTitle.length} \leq 7\)
- `columnTitle` consists only of **uppercase English letters**.
- `columnTitle` is in the range `["A", "FXSHRXW"]`.

---

## Algorithm

1. **Understand the Problem as Base-26 Conversion**:
   - Each letter in `columnTitle` represents a digit in a base-26 number system.
   - The leftmost letter contributes the most significant value, similar to how numbers are represented in base-10.

2. **Steps to Solve**:
   - Initialize `columnNumber` to `0`.
   - Iterate over each character in `columnTitle`:
     - Convert the character to a number using the formula:  
       `value = (ord(char) - ord('A') + 1)`.
     - Multiply the current `columnNumber` by `26` and add the computed value.
   - Continue until all characters are processed.

3. **Return the Result**:
   - The final computed `columnNumber` is the corresponding column index.

---

## Complexity

- **Time Complexity**:  
  \(O(n)\), where `n` is the length of `columnTitle`.

- **Space Complexity**:  
  \(O(1)\), since only a few integer variables are used.
