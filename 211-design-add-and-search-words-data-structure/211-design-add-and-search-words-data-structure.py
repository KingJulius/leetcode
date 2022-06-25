class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True
                  
    
    def search(self, word: str) -> bool:
        def solve(index, root):
            curr = root
            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if solve(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.end_of_word
        return solve(0, self.root)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)