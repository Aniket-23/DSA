# Missing Number Algorithm

## Overview
The **Missing Number Algorithm** efficiently identifies the missing integer in an array that contains `n` distinct numbers from the range `[0, n]`. The objective is to determine which number is absent.

## Problem Statement
Given an array of `n` unique numbers within the range `[0, n]`, exactly **one** number is missing. The challenge is to find this missing value using an optimal approach.

## Approach

### **1. Iterative Search Method**
- Traverse the possible values in the range `[0, n]`.
- Check each number to see if it exists in the array.
- Return the first missing number.

**Pros:**
- Simple to understand.
- Works for any dataset.

**Cons:**
- Time complexity is **O(n²)** due to repeated membership checks.

## Complexity Analysis
| Approach | Time Complexity | Space Complexity |
|----------|---------------|------------------|
| Iterative Search | O(n²) | O(1) |

---