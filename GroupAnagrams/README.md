# Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Algorithm

1. Initialize a dictionary (hash map) to group strings by their sorted version.
2. For each string in the input list:
   - Sort the characters of the string alphabetically.
   - Use the sorted string as the key in the dictionary.
   - Append the original string to the list corresponding to that key.
3. Return the **values** of the dictionary, which will be lists of grouped anagrams.

**Time Complexity:** O(N * K log K)  
Where N is the number of strings and K is the maximum length of a string (due to sorting).

**Space Complexity:** O(N * K)  
To store the grouped anagrams.

---