class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # frequency tuple : indices of strs
        for i in range(len(strs)):
            freq_arr = [0] * 26 # O(26)
            for c in strs[i]:
                index = ord(c) - ord('a')
                freq_arr[index] += 1 

            freq_tuple = tuple(freq_arr)
            if freq_tuple in map.keys():
                map[freq_tuple].append(strs[i])
            else:
                map[freq_tuple] = [strs[i]]
        
        return [indices for indices in map.values()]
