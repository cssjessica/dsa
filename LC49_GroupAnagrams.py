class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity: O(m *n * 26) => O(m * n)

        res = defaultdict(list)

        # m
        for s in strs:
            count = [0] * 26 # a . . . z
            
            # n
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            res[tuple(count)].append(s)
            
        return res.values()
