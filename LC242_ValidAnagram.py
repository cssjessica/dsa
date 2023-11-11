class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
            
        s_count, t_count = {}, {}

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        for j in s_count:
            if s_count[j] != t_count.get(j, 0):
                return False
                
        return True     
