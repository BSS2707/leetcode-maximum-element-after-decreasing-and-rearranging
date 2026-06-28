class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1] + 1)
        return arr[-1]
s = Solution()
print(s.maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))   # 2
print(s.maximumElementAfterDecrementingAndRearranging([100,1,1000])) # 3
print(s.maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))  # 5
