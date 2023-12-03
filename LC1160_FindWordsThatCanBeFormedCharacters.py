class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # time complexity: O(nk+m)
        # space complexity: O(n+m)

        count = Counter(chars)
            
        res = 0
            
        for word in words:
            cur_word = defaultdict(int)
            good = True
            for c in word:
                cur_word[c] += 1
                if c not in count or cur_word[c] > count[c]:
                    good = False
                    break
            if good:
                res += len(word)

        return res
