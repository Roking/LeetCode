class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        if s.find(" ") < 0:
            return len(s)
        lis = s.split(" ")
        return len(lis[len(lis)-1])