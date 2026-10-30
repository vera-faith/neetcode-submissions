class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        for n in s:
            countS[n] = countS.get(n, 0) + 1 

        countT = {}
        for n in t:
            countT[n] = countT.get(n, 0) + 1

        return countS == countT
