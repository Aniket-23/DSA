# Climbing Stairs Problem

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top. 

Each time you can either climb **1 step** or **2 steps**. The task is to determine the total number of distinct ways you can climb to the top.

---

## Examples

### Example 1:
**Input**:  
`n = 2`  

**Output**:  
`2`  

**Explanation**:  
There are two ways to climb to the top:
1. 1 step + 1 step  
2. 2 steps  

---

### Example 2:
**Input**:  
`n = 3`  

**Output**:  
`3`  

**Explanation**:  
There are three ways to climb to the top:
1. 1 step + 1 step + 1 step  
2. 1 step + 2 steps  
3. 2 steps + 1 step  

---

## Constraints

- \(1 \leq n \leq 45\)

---

## Algorithm

1. **Understand the Problem as a Fibonacci Sequence**:
   - The number of ways to reach step `n` is equal to the sum of the ways to reach step `n-1` and step `n-2` because:
     - You can reach step `n` from `n-1` by taking 1 step.
     - You can reach step `n` from `n-2` by taking 2 steps.

2. **Base Cases**:
   - If `n = 1`, there is only **1 way** to climb the staircase.
   - If `n = 2`, there are **2 ways** to climb the staircase.

3. **Iterative Approach**:
   - Start with the base cases.
   - For each step from `3` to `n`, calculate the total number of ways by adding the ways to reach the previous two steps.

4. **Return the Result**:
   - The result for `n` is stored after calculating all steps iteratively.

---

## Complexity

- **Time Complexity**:  
  \(O(n)\), as we calculate the ways for each step from `1` to `n`.

- **Space Complexity**:  
  \(O(1)\), since only a constant amount of space is used to store the intermediate results.

