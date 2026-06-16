class TrieNode:
    def __init__(self):
        # self.parent = None
        self.letters = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Add all words to the trie

        trie = TrieNode()
        for word in words:
            ptr = trie
            for c in word:
                if c not in ptr.letters:
                    ptr.letters[c] = TrieNode()
                
                # ptr.letters[c].parent = ptr
                ptr = ptr.letters[c]

            ptr.isWord = True
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        currWord = []
        wordsFound = []
        
        def dfs(i, j, currTrie):
            if currTrie and currTrie.isWord:
                wordsFound.append(''.join(currWord))        

            if (i,j) in visited or not currTrie \
            or i < 0 or i >= ROWS \
            or j < 0 or j >= COLS \
            or board[i][j] not in currTrie.letters:
                return
            
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            visited.add((i,j))
            currWord.append(board[i][j])
            for di, dj in dirs:
                dfs(i + di, j + dj, currTrie.letters[board[i][j]])
            currWord.pop()
            visited.remove((i,j))
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie)
        
        return list(set(wordsFound))