class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i, dst in enumerate(edges):
            adj[i].append(dst)
            
        def bfs(src, dist_map):
            q = deque()
            q.append([src, 0])
            dist_map[src] = 0
            while q:
                node, dist = q.popleft()
                for nei in adj[node]: # change to edges
                    if nei not in dist_map:
                        q.append([nei, dist + 1])
                        dist_map[nei] = dist + 1
                        
        node1Dist = {} # map node -> distance from node1
        node2Dist = {} # map node -> distance from node2
        bfs(node1, node1Dist)
        bfs(node2, node2Dist)

        res = -1
        res_dist = float("inf")
        for i in range(len(edges)):
            if i in node1Dist and i in node2Dist:
                dist = max(node1Dist[i], node2Dist[i])
                if dist < res_dist:
                    res = i
                    res_dist = dist
                    
        return res
