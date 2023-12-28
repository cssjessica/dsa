class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # time complexity: O(n)
        # space complexity: O(n)

        cities = set()
        for p in paths:
            cities.add(p[0])

        for p in paths:
            if p[1] not in cities:
                return p[1]
