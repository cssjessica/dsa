class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # idx = -1
        # min_dist = float('inf')
        # if len(points) > 1:
        #     min_dist = abs(x - points[0][0]) + abs(y - points[0][1])
        #     for i in range(1, len(points)):
        #         if x == points[i][0] or y == points[i][1]:
        #             dist = abs(x - points[i][0]) + abs(y - points[i][1])
        #             if dist < min_dist:
        #                 min_dist = dist
        #                 idx = i
        #     return idx
        # else:
        #     if x == points[0][0] or y == points[0][1]:
        #         return 0
        #     else:
        #         return -1

        idx = -1
        min_dist = float('inf')
        for i, p in enumerate(points):
            if x == p[0] or y == p[1]:
                dist = abs(x - p[0]) + abs(y - p[1])
                if dist < min_dist:
                    min_dist = dist
                    idx = i
        return idx




