class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time complexity: O(nlogn) + O(n) => O(nlogn)

        intervals.sort()

        if not intervals:
            return []
            
        # cur = intervals[0]
        # res = []
        res = [intervals[0]]

        for pair in intervals:
            cur = res[-1]
            if cur[1] >= pair[0]:
                # cur[1] = = max(cur[1], pair[1])
                res[-1][1] = max(cur[1], pair[1])
            else:
                res.append(pair)
                # res.append(cur)
                # cur = pair
        # res.append(cur)
        return res
