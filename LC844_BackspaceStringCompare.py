class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_final, t_final = [], []
        for char in s:
            if char == "#":
                if s_final:
                    s_final.pop()
            else:
                s_final.append(char)
        
        for char in t:
            if char == "#":
                if t_final:
                    t_final.pop()
            else:
                t_final.append(char)
        
        if s_final == t_final:
            return True
        else:
            return False
