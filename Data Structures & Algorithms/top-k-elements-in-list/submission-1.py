class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for num, cnt in freq.items():
            buckets[cnt].append(num)

        res = []
        for freq_val in range(n, 0, -1):
            for num in buckets[freq_val]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res



        