class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # check if the order of the words is right
        # Time complexity: len(words)*len(char)
        # first differing char
        # if word A is prefix of word B, word B must be after word A

        # hash map
        order_idx = {c: i for i, c in enumerate(order)}

        # compare every adjacent pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            
            for j in range(len(w1)):
                # if a word is a prefix of the other in the wrong order
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    # if a character in word 1 comes after a character in word 2
                    if order_idx[w1[j]] > order_idx[w2[j]]:
                        return False
                    # if the characters are not the same but the order is ok, get out of the inner loop
                    break
        return True
		
		
