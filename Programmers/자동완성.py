class TrieNode:
    def __init__(self):
        self.cnt = 1
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            else:
                node.children[c].cnt += 1
            node = node.children[c]

    def search(self, words):
        res_cnt = 0
        for word in words:
            cnt = 0
            node = self.root
            for c in word:
                cnt += 1
                if node.children[c].cnt == 1:
                    break
                else:
                    node = node.children[c]
            res_cnt += cnt
        return res_cnt

def solution(words):
    T = Trie()
    for w in words:
        T.insert(w)
    return T.search(words)