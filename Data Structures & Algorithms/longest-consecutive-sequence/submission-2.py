class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = 1

        if len(nums) == 0:
            return 0

        for num in nums:
            if num - 1 in nums:
                continue
            curr_length = 1
            curr = num

            while curr + 1 in nums:
                curr_length += 1
                curr += 1
            
            if curr_length > length:
                length = curr_length

        return length

        
            
            
        