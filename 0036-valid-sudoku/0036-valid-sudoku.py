class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validate a 9x9 Sudoku board.
        """
        # TC: O(1), SC: O(1) — board size is fixed (9x9), so operations are constant time and space
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                box_idx = (row // 3) * 3 + (col // 3)

                if (
                    val in rows[row] or
                    val in cols[col] or
                    val in boxes[box_idx]
                ):
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box_idx].add(val)

        return True

