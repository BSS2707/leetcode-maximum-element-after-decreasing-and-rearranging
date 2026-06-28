# leetcode-maximum-element-after-decreasing-and-rearranging
# Maximum Element After Decrementing and Rearranging

This repository contains my solution to the LeetCode problem **Maximum Element After Decrementing and Rearranging**.

---

## 📖 Problem Statement
You are given an array of positive integers `arr`. Perform operations so that:

1. The first element in `arr` must be `1`.
2. The absolute difference between any two adjacent elements must be ≤ 1.
3. Allowed operations:
   - Decrease any element to a smaller positive integer.
   - Rearrange elements in any order.

Return the maximum possible value of an element in `arr` after performing the operations.

---

## ✅ Approach
- Sort the array.
- Force the first element to `1`.
- For each subsequent element:
  - Set it to `min(arr[i], arr[i-1] + 1)`.
- The last element will be the maximum possible value.

This ensures the array grows step by step without violating the conditions.

---

## 💻 Python Solution

```python
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1] + 1)
        return arr[-1]
s = Solution()
print(s.maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))   # Output: 2
print(s.maximumElementAfterDecrementingAndRearranging([100,1,1000])) # Output: 3
print(s.maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))  # Output: 5

