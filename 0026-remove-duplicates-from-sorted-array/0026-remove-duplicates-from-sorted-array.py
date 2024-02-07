class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        pointer = 0

        for i in range(len(nums)):
            if (nums[i] != nums[pointer]):
                pointer += 1
                nums[pointer] = nums[i]
                ans += 1

        return ans
