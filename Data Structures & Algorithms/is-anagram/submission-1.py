class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for ch in s:
            if ch in s_map:
                s_map[ch] += 1
            else:
                s_map[ch] = 1

        for ch in t:
            if ch in t_map:
                t_map[ch] += 1
            else:
                t_map[ch] = 1

        for ch in s_map:
            if (ch not in s_map) or (ch not in t_map):
                return False
                
            if s_map[ch] != t_map[ch]:
                return False
        return True
        