class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)

        answer = [-1 for i in range(n)]
        q = deque()
        q.append([0, 0, None])  # [node, length, prev edge color]
        visit = set()
        visit.add((0, None))
        while q:
            node, length, edge_color = q.popleft()
            if answer[node] == -1:
                answer[node] = length

            if edge_color != "red":
                for nei in red[node]:
                    if (nei, "red") not in visit:
                        visit.add((nei, "red"))
                        q.append([nei, length + 1, "red"])

            if edge_color != "blue":
                for nei in blue[node]:
                    if ((nei, "blue")) not in visit:
                        visit.add((nei, "blue"))
                        q.append([nei, length + 1, "blue"])
        
        return answer

