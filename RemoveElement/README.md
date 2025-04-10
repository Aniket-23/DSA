# Remove Element

## Problem Statement

Given an integer array `nums` and an integer `val`, **remove all occurrences** of `val` in-place.  
The order of elements **may be changed**, and the remaining elements beyond the first `k` positions do **not matter**.

Return the number of elements in `nums` that are **not equal to** `val`.

---

## Custom Judge (How Your Solution Will Be Evaluated)

The judge will test your solution with code similar to:

```java
int[] nums = [...];         // Input array
int val = ...;              // Value to remove
int[] expectedNums = [...]; // The expected output with correct length, no values equal to val

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort first k elements
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, your solution will be accepted.

## Constraints

- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

---

## Algorithm

1. **Initialization**: Start with a pointer `i = 0` which will keep track of the next position to store a valid element (i.e., an element that is not equal to `val`).
2. **Iterate through the array**: Use a second pointer `j` to iterate through the array:
   - If `nums[j] != val`, assign `nums[i] = nums[j]`, and increment `i`.
   - If `nums[j] == val`, skip the element (do nothing).
3. **End of iteration**: After completing the loop, the first `i` elements of `nums` will contain the values that are not equal to `val`.
4. **Return `i`**: The number of valid elements (non-equal to `val`) is `i`, so return it.

### Time Complexity
- O(n), where n is the length of the `nums` array, since we iterate through the array once.

### Space Complexity
- O(1), because the algorithm works in-place without using extra space.
