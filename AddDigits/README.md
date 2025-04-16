# Single Digit Sum

## Problem Statement
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

## Examples

### Example
**Input:** 
num = 38

**Output:** 
2

**Explanation:**  
The process is as follows:
38 --> 3 + 8 = 11 11 --> 1 + 1 = 2

Since `2` has only one digit, return it.


## Constraints
- `0 <= num <= 2^31 - 1`

## Solution Approach
One way to solve this problem efficiently is using the digital root formula:
digital_root = 1 + (num - 1) % 9

This formula provides an O(1) solution instead of repeatedly summing the digits in a loop.

# Example usage
print(addDigits(38))  # Output: 2
print(addDigits(0))   # Output: 0