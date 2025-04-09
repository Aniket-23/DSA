# Problem: Count Operations to Obtain Zero

You are given two non-negative integers `num1` and `num2`.

In one operation, do the following:
- If `num1 >= num2`, subtract `num2` from `num1`.
- Otherwise, subtract `num1` from `num2`.

For example:
- If `num1 = 5` and `num2 = 4`, subtract `num2` from `num1`, resulting in `num1 = 1` and `num2 = 4`.
- If `num1 = 4` and `num2 = 5`, subtract `num1` from `num2`, resulting in `num1 = 4` and `num2 = 1`.

Return the number of operations required to make either `num1 = 0` or `num2 = 0`.

---

## Algorithm

To solve the problem, follow these steps:

1. **Initialize a counter** to keep track of the number of operations performed.
2. **Repeat the following steps** until either `num1` or `num2` becomes zero:
   - If `num1 >= num2`, subtract `num2` from `num1`.
   - Else, subtract `num1` from `num2`.
   - Increment the operation counter by 1.
3. **Return the counter** as the result — this is the total number of operations performed until one of the numbers becomes zero.

### Time Complexity:
- **Worst-case**: O(max(num1, num2)) operations
- Each operation decreases one of the numbers, so the loop can run at most `max(num1, num2)` times.

### Space Complexity:
- **O(1)** — only a few variables are used regardless of input size.