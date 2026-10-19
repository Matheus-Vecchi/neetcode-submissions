class TrieNode:
    def __init__(self):
        self.child = {}
        self.isLeaf = False

class PrefixTree:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.isLeaf = True


    def search(self, word: str) -> bool:
        curr = self.node
        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        if curr.isLeaf:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return True
        