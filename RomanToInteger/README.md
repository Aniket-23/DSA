# Roman to Integer

## Problem Description

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

### Explanation of Roman Numerals

1. Numbers are generally written from largest to smallest, from left to right. 
   - Example: `II = 2`, `XII = 12`, `XXVII = 27`.

2. **Subtractive Notation**: When a smaller numeral appears before a larger numeral, it is subtracted.
   - Example: `IV = 4`, `IX = 9`.
   - Subtractive pairs:
     - `I` can be placed before `V (5)` and `X (10)` to form `4` and `9`.
     - `X` can be placed before `L (50)` and `C (100)` to form `40` and `90`.
     - `C` can be placed before `D (500)` and `M (1000)` to form `400` and `900`.

### Examples

#### Example 1:
**Input**: `s = "III"`  
**Output**: `3`  
**Explanation**: `III = 3`.

#### Example 2:
**Input**: `s = "LVIII"`  
**Output**: `58`  
**Explanation**: `L = 50`, `V = 5`, `III = 3`.

#### Example 3:
**Input**: `s = "MCMXCIV"`  
**Output**: `1994`  
**Explanation**: `M = 1000`, `CM = 900`, `XC = 90`, and `IV = 4`.

---

## Constraints

- \( 1 \leq s.length \leq 15 \)
- \( s \) contains only the characters: `'I', 'V', 'X', 'L', 'C', 'D', 'M'`.
- It is guaranteed that \( s \) is a valid Roman numeral within the range `[1, 3999]`.

## Objective

Given a Roman numeral, convert it to an integer.