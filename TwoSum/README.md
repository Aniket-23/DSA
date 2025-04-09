# Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you **may not use the same element twice**.

You can return the answer in any order.

---

## Examples

### Example 1:
**Input:**

nums = [2,7,11,15], target = 9


**Output:**

[0,1]


**Explanation:**
Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

### Example 2:
**Input:**

nums = [3,2,4], target = 6

**Output:**

[1,2]

**Explanation:**
Because `nums[1] + nums[2] == 6`, we return `[1, 2]`.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

---

## Algorithm Overview

1. Initialize an empty hash map to store previously seen numbers and their indices.
2. Iterate through each number in the array:
   - Compute the complement: `target - current number`.
   - If the complement exists in the hash map, return the current index and the index of the complement.
   - Otherwise, store the current number and its index in the hash map.
3. Return the pair of indices that sum up to the target.

---

## Time and Space Complexity

- **Time Complexity:** O(n)  
  Only a single pass through the array is needed.

- **Space Complexity:** O(n)  
  In the worst case, we may need to store all elements in the hash map.

---