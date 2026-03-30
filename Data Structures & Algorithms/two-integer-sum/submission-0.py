class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in complementMap.keys():
                return [complementMap[difference], i]
            complementMap[nums[i]] = i
            
        return []