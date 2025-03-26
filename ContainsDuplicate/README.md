# Contains Duplicate

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least **twice** in the array, and return `false` if every element is distinct.

## Algorithm:

1. **Convert List to Set**  
   - Create a set from the `nums` array to remove duplicate values automatically.

2. **Compare Lengths**  
   - If the length of the set is **equal** to the length of the original array, return `False` (no duplicates exist).
   - Otherwise, return `True` (duplicates exist).

## Complexity Analysis:
- **Time Complexity:** `O(n)`, since converting a list to a set takes `O(n)`, and checking the length is `O(1)`.  
- **Space Complexity:** `O(n)`, as the set stores unique elements separately.
