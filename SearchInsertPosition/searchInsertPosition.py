class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if nums[0] > target:
            return 0 

        for i in range(0, len(nums) - 1):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i + 1] > target:
                    return i + 1

        if nums[-1] == target:
            return len(nums) - 1
        else:
            return len(nums)
        

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low