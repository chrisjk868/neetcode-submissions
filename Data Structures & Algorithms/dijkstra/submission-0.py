class Solution:
    import heapq
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Construct an adjacency list:
        adj = {i: [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
        # Cost map contains the shortest distance to every node (0 -> n - 1) starting from the source node
        cost_map = {}
        # Perform Dijkstra's algorithm here
        pq = [(0, src)]
        heapq.heapify(pq)
        while pq:
            cur_cost, node = heapq.heappop(pq)
            # If our current node is in the cost map that means we have processed it before so we continue
            if node in cost_map:
                continue
            # If our current node is not in the cost map and we reach it:
            # This means that we have so far taken the path of minimal to cost to reach our current node
            # Therefore we can directly add it to the cost map which marks it as visited and processed
            cost_map[node] = cur_cost
            # Process our current node's neighbors
            for nei, nei_cost in adj[node]:
                # There exists a chance that we consider previously visited nodes
                # So we wouldn't want to process those nodes again as we know that they already obtained their lowest cost path
                if nei not in cost_map:
                    heapq.heappush(pq, (cur_cost + nei_cost, nei))
        # Since some nodes aren't reachable we would have to process them also
        for i in range(n):
            if i not in cost_map:
                cost_map[i] = -1
        return cost_map
