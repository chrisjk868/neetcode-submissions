class     Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Get all edges for each character for currently sorted order of words
        chars = {c for w in words for c in w}
        edges = set()
        for i in range(1, len(words)):
            prev, cur = words[i - 1], words[i]
            min_len = min(len(prev), len(cur))
            if len(prev) > len(cur) and prev[:min_len] == cur[:min_len]:
                return ""
            for j in range(min_len):
                if prev[j] != cur[j]:
                    edges.add((prev[j], cur[j]))
                    break

        # After we get all edges construct an adjacency list
        adj = {c: [] for c in chars}
        for u, v in edges:
            adj[u].append(v)

        # Use DFS to find any self loops
        visited = set() # 0: unvisited, 1: visiting, 2: visited
        visiting = set()
        res = []
        def dfs(cur):
            if cur in visiting:
                return False
            if cur in visited:
                return True
            
            visiting.add(cur)
            for neighbor in adj[cur]:
                if not dfs(neighbor):
                    return False
            visiting.remove(cur)
            visited.add(cur)
            res.append(cur)
            return True
        
        for c in chars:
            if c not in visited:
                if not dfs(c):
                    return ""

        return "".join(res[::-1])