class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for n in range(len(accounts)):
            wealth.append(sum(accounts[n][:]))
        return max(wealth)

