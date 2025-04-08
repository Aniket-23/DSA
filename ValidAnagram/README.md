# Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

---

## Algorithm

To determine if two strings `s` and `t` are anagrams:

1. **Use Frequency Counter:**
   - Create a frequency count (dictionary) of all characters in string `s`.
   - Do the same for string `t`.

2. **Compare Frequency Maps:**
   - If both frequency dictionaries are identical, then `t` is an anagram of `s`.

3. **Return Result:**
   - Return `true` if the counters match.
   - Otherwise, return `false`.

### Tools Used:
- Python's `collections.Counter` is used to quickly create frequency maps of characters from both strings.

### Time and Space Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the input strings (assuming both are the same length).
- **Space Complexity:** `O(1)`, since the maximum number of different lowercase letters is constant (26).
