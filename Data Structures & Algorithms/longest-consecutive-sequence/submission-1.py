class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1
        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            curr_length = 1
            curr = nums[i]

            while curr + 1 in nums:
                curr_length += 1
                curr += 1

            if curr_length > length:
                length = curr_length

        return length
            


        