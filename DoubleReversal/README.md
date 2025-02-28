# A Number After a Double Reversal

## Problem Description

Reversing an integer means rearranging its digits in reverse order.  
- For example, reversing `2021` gives `1202`.  
- Leading zeros are not retained. For example, reversing `12300` results in `321`.

Given an integer `num`, follow these steps:
1. Reverse `num` to get `reversed1`.
2. Reverse `reversed1` to get `reversed2`.
3. Return `true` if `reversed2` equals `num`, otherwise return `false`.

---

## Examples

### Example 1:
**Input**:  
`num = 526`  

**Output**:  
`true`  

**Explanation**:  
- Reverse `526` → `625`
- Reverse `625` → `526`  
- Since `526` equals `num`, return `true`.

---

### Example 2:
**Input**:  
`num = 1800`  

**Output**:  
`false`  

**Explanation**:  
- Reverse `1800` → `81` (leading zeros removed)
- Reverse `81` → `18`  
- Since `18` does not equal `num`, return `false`.

---

### Example 3:
**Input**:  
`num = 0`  

**Output**:  
`true`  

**Explanation**:  
- Reverse `0` → `0`
- Reverse `0` → `0`  
- Since `0` equals `num`, return `true`.

---

## Constraints

- \(0 \leq \text{num} \leq 10^6\)

---

## Algorithm

1. **Reverse the number `num`**:
   - Extract each digit and construct the reversed number.
   - Ignore leading zeros when reversing.

2. **Reverse the reversed number (`reversed1`) again**:
   - Follow the same reversing process.

3. **Compare the final reversed number (`reversed2`) with `num`**:
   - If `reversed2 == num`, return `true`; otherwise, return `false`.

---

## Complexity

- **Time Complexity**:  
  \(O(\log_{10}(\text{num}))\), as we process each digit in the number.

- **Space Complexity**:  
  \(O(1)\), since only a few integer variables are used.
