class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = len(string)
            res += str(length) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr_index = 0

        while curr_index < len(s):
            length = ""
            string = ""
            # First find the length, fetch all the chars before #
            while s[curr_index] != "#":
                length += s[curr_index]
                curr_index += 1 

            length = int(length)

            curr_index += 1
            for i in range(curr_index, curr_index + length):
                string += s[i]
                curr_index += 1

            res.append(string)

        return res



        
        






