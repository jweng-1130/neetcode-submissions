class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, value in enumerate(nums):
            diff = target - nums[index]
            if diff not in prevMap:
                prevMap[value] = index
            else:
                return [prevMap[diff], index]

