# Excel Sheet Column Title

## Problem Description

Given an integer `columnNumber`, the task is to return its corresponding column title as it appears in an Excel sheet.

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
`columnNumber = 1`  

**Output**:  
`"A"`  

---

### Example 2:
**Input**:  
`columnNumber = 28`  

**Output**:  
`"AB"`  

---

### Example 3:
**Input**:  
`columnNumber = 701`  

**Output**:  
`"ZY"`  

---

## Constraints

- \(1 \leq \text{columnNumber} \leq 2^{31} - 1\)

---

## Algorithm

1. **Understand the Problem as Base-26 Conversion**:
   - Excel columns are similar to a base-26 numbering system, but it is 1-indexed.  
   - Subtract `1` from the column number to handle the 1-indexed nature effectively.

2. **Steps to Solve**:
   - While `columnNumber > 0`:
     - Subtract `1` from `columnNumber`.
     - Find the remainder when `columnNumber` is divided by `26`. This remainder gives the current character:
       - `0 -> A`, `1 -> B`, ..., `25 -> Z`.
     - Append the corresponding character to the result.
     - Divide `columnNumber` by `26` to move to the next "digit."
   - Reverse the result at the end to form the correct column title.

3. **Return the Result**:
   - Combine all the characters and return the reversed string as the final column title.

---

## Complexity

- **Time Complexity**:  
  \(O(\log_{26}(\text{columnNumber}))\), as we divide the column number by `26` at each step.

- **Space Complexity**:  
  \(O(\log_{26}(\text{columnNumber}))\), for storing the result string.
