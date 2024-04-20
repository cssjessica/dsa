class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)

        for s in strs:	
            m_cnt, n_cnt = s.count("0"), s.count("1")
            for mm in range(m, m_cnt - 1, -1):
                for nn in range(n, n_cnt - 1, -1):
                    dp[(mm, nn)] = max(1+dp[(mm-m_cnt, nn-n_cnt)], dp[(mm,nn)])
                    
        return dp[(m,n)]
