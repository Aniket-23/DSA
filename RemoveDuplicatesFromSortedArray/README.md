# Remove Duplicates from Sorted Array

## Problem Statement

Given an integer array `nums` **sorted in non-decreasing order**, remove the **duplicates in-place** such that each unique element appears only **once**. The relative order of the elements should be preserved.

After removing the duplicates:
- Place the unique elements in the first `k` slots of the array.
- Return the number `k`, which represents the count of unique elements.

**Note:** The remaining elements beyond the first `k` positions do not matter.

---

## Custom Judge (How Your Solution Will Be Evaluated)

The platform will run something like this to test your function:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // Expected array with unique elements only

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, the solution is accepted.

## Constraints

- 1 <= nums.length <= 3 * 10⁴  
- -100 <= nums[i] <= 100  
- nums is sorted in non-decreasing order  
- The function must run in O(n) time and use O(1) extra space.

---

## Algorithm

1. Initialize a pointer `i = 1` to mark the position of the next unique element.
2. Iterate through the array with another pointer `j` starting from index 1.
3. For each `j`, compare `nums[j]` with `nums[i - 1]`:
   - If they are different, assign `nums[i] = nums[j]` and increment `i`.
   - If they are the same, it means the value is a duplicate, so skip it.
4. After the loop ends, the first `i` elements in `nums` will be the unique elements.
5. Return `i` as the count of unique elements.

### Time Complexity
- O(n), where n is the length of `nums` — we iterate through the array once.

### Space Complexity
- O(1), as the operation is done in-place without using extra space.
