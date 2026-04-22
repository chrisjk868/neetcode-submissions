class     Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Get all characters of current word list
        chars = {c for w in words for c in w}
        edges = set()
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ''
            for j in range(min_len):
                if w1[j] != w2[j]:
                    edges.add((w1[j], w2[j]))
                    break

        adj = {c: [] for c in chars}
        for u, v in edges:
            adj[u].append(v)

        visited = set()
        visiting = set()
        path = []
        def dfs(cur):
            if cur in visiting:
                return False

            if cur in visited:
                return True

            visiting.add(cur)
            for nxt in adj[cur]:
                if not dfs(nxt):
                    return False

            visiting.remove(cur)
            visited.add(cur)
            path.append(cur)
            return True

        for cur, _ in adj.items():
            if cur not in visited:
                if not dfs(cur):
                    return ''

        return ''.join(path[::-1])

        

