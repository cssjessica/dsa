class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))]

        for i in range(len(pairs)):
            m_score, m_age = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if m_age >= age:
                    dp[i] = max(dp[i], m_score + dp[j])
        return max(dp)
