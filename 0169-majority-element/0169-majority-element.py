class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        criteria = len(nums) / 2
        cnt = 0

        nums = sorted(nums)
        for i in range(len(nums)):
            cnt += 1
            if cnt > criteria: return nums[i]
            if nums[i] != nums[i+1]: cnt = 0
        