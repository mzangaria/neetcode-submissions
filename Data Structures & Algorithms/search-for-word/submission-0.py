class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def search(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if r < 0 or r == rows or c < 0 or c == cols:
                return False
            
            if (r,c) in visited:
                return False
            
            if board[r][c] != word[i]:
                return False
            
            visited.add((r,c))

            found = (
                search(r + 1, c, i + 1) or
                search(r - 1, c, i + 1) or
                search(r, c + 1, i + 1) or
                search(r, c - 1, i + 1)
            )

            visited.remove((r,c))

            return found
        
        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0):
                    return True
        
        return False