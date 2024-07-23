# Problem: You have to ensure that 4 queens don't attack each other in a chess board.

class Solution:
    def solveNQueens(self, size: int) -> list[list[str]]:
        col = set()
        posDiagonal = set()
        negDiagonal = set()

        result = []
        board = [["."] * size for i in range(size)]

        def backstrack(row):
            if row == size:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return         
            for column in range(size):
                if column in col or (row + column) in posDiagonal or (row - column) in negDiagonal:
                    continue

                col.add(column)
                posDiagonal.add(row + column)
                negDiagonal.add(row - column)

                board[row][column] = "Q"

                backstrack(row + 1)

                col.remove(column)
                posDiagonal.remove(row + column)
                negDiagonal.remove(row - column)

                board[row][column] = "."

        backstrack(0)
        return result
    

s = Solution()
print(s.solveNQueens(4))




