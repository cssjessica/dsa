class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # # s1 = 'bank'
        # # s2 = 'kanb'
        # # dictionary_1 = {b:k, k:b}
        # # dictionaty_2 = {k:b, b:k}

        # dictionary_1 = {}
        # dictionary_2 = {}

        # for i in range(len(s1)):
        #     if s1[i] == s2[i]:
        #         pass
        #     else:
        #         dictionary_1[s1[i]] = s2[i]
        #         dictionary_2[s2[i]] = s1[i]
        # if dictionary_1 == dictionary_2 and len(dictionary_1) <= 2:
        #     return True
        # else:
        #     return False

        # or
        if collections.Counter(s1) != collections.Counter(s2):
            return False

        diff = 0
        for x, y in zip(s1, s2):
            if x != y:
                diff += 1
        return diff <= 2
