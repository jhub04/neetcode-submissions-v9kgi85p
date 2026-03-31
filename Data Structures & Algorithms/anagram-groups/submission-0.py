class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # sorted string : indices of strs
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in map.keys():
                map[sorted_str].append(strs[i])
            else:
                map[sorted_str] = [strs[i]]

        return [indices for indices in map.values()]