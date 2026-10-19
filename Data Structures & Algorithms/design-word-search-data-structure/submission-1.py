class TrieNode:
    def __init__(self):
        self.child = {}
        self.leaf = False

class WordDictionary:
    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c != "." and c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.leaf = True

    def search(self, word: str, start=None, i=0) -> bool:
        if not start:
            curr = self.node
        else:
            curr = start
        while i < len(word):
            if word[i] == ".":
                for key in curr.child.keys():
                    if self.search(word, curr.child[key], i+1):
                        return True
                return False
            else:
                if word[i] not in curr.child:
                    return False
                curr = curr.child[word[i]]
                i += 1
        return curr.leaf
    
