class TrieNode:
    def __init__(self, val='', is_end=False):
        self.val = val
        self.children = {}
        self.is_end = is_end

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            
            node = node.children[c]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.children: return False
            node = node.children[c]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.children: return False
            node = node.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
