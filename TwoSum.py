class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for i in range(len(nums)):
            if nums[i] in store:
                return store[nums[i]], i
            else:
                store[target - nums[i]] = i
