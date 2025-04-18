# Search Insert Position

## Problem Statement

Given a **sorted array** of **distinct integers** and a **target** value, return the **index** if the target is found.  
If not, return the index where it would be if it were **inserted in order**.

You must implement an algorithm with **O(log n)** runtime complexity.

---

## Example

### Example 1
**Input:**  
`nums = [1,3,5,6], target = 5`  
**Output:**  
`2`

### Example 2
**Input:**  
`nums = [1,3,5,6], target = 2`  
**Output:**  
`1`

### Example 3
**Input:**  
`nums = [1,3,5,6], target = 7`  
**Output:**  
`4`

---

## Constraints

```markdown
- 1 <= nums.length <= 10⁴
- -10⁴ <= nums[i] <= 10⁴
- nums contains **distinct** values
- nums is sorted in **ascending** order
- -10⁴ <= target <= 10⁴

## Algorithm

1. First, check if the target is less than the first element:
   - If yes, return 0 (it should be inserted at the beginning).
2. Loop through the array from index 0 to n - 2:
   - If `nums[i] == target`, return i.
   - If `nums[i] < target < nums[i + 1]`, return i + 1.
3. After the loop:
   - If `nums[-1] == target`, return the last index.
   - Otherwise, return `len(nums)` — insert at the end.

📝 Note: While this approach works for small inputs, it is a linear search (O(n)) and **does not meet the O(log n)** requirement as specified in the problem. A binary search should be used for full compliance.


## Algorithm 2

1. Initialize two pointers:
   - `low = 0` — the start of the search range
   - `high = len(nums) - 1` — the end of the search range

2. Perform binary search using a while loop:
   - While `low <= high`:
     - Compute the middle index: `mid = (low + high) // 2`
     - If `nums[mid] == target`, return `mid` (target found)
     - If `nums[mid] > target`, reduce the search range to the left half by setting `high = mid - 1`
     - If `nums[mid] < target`, search in the right half by setting `low = mid + 1`

3. If the loop ends without finding the target, return `low`
   - This is the correct index where `target` would be inserted to maintain sorted order

### Time Complexity
- **O(log n)** due to binary search

### Space Complexity
- **O(1)** — constant extra space used
