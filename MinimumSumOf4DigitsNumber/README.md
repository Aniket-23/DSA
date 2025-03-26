# Minimum Sum of Split Digits

## Problem Statement
You are given a positive integer `num` consisting of exactly four digits. The goal is to split `num` into two new integers `new1` and `new2` by using all the digits found in `num`. 

- Leading zeros are allowed in `new1` and `new2`.
- All four digits must be used exactly once.
- The objective is to return the **minimum possible sum** of `new1` and `new2`.

## Algorithm: Minimum Sum of Split Digits

1. **Extract Digits**  
   - Convert the given integer `num` into a string.  
   - Extract all four digits and store them in a list.  

2. **Sort the Digits**  
   - Sort the list in ascending order to ensure the smallest digits are used optimally.  

3. **Form Two Numbers**  
   - Construct `num1` using the **smallest** and **third smallest** digits.  
   - Construct `num2` using the **second smallest** and **largest** digits.  
   - This ensures that both numbers are as small as possible to minimize their sum.  

4. **Compute the Sum**  
   - Add `num1` and `num2` together to get the result.  

5. **Return the Minimum Sum**  
   - The final result is returned as the minimum possible sum.
