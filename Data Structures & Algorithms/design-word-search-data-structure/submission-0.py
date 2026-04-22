class WordNode:
    def __init__(self, char):
        self.char = char
        self.next = dict()
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode('')

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.next:
                cur.next[word[i]] = WordNode(word[i])
            cur = cur.next[word[i]]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(idx, cur):
            if idx >= n:
                if cur.isEnd:
                    return True
                else:
                    return False
            if word[idx] == '.':
                results = False
                for c in cur.next:
                    results = results or dfs(idx + 1, cur.next[c])
                return results
            if word[idx] not in cur.next:
                return False
            else:
                return dfs(idx + 1, cur.next[word[idx]])
        ans = dfs(0, self.root)
        return ans