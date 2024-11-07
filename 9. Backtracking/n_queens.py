type Board = list[list[bool]]


def queens(n: int) -> Board | None:
    board: Board = [[False for _ in range(n)] for _ in range(n)]
    return solve(board, 0)


def solve(board: Board, col: int) ->  Board | None:
    if col == len(board):
        return board
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True
            result: Board | None = solve(board, col + 1)
            if result:
                return result
            board[row][col] = False
    return None


def is_safe(board: Board, row: int, col: int) -> bool:
    # Is there another queen in the same row?
    for i in range(0, col):
        if board[row][i]:
            return False

    # Is there another queen in upper left diagonal?
    for i, j in zip(range(row - 1, -1, -1),
                    range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    # If there another queen in lower left diagonal?
    for i, j in zip(range(row + 1, len(board), 1),
                    range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    return True


def print_board(board: Board) -> None:
    for row in board:
        for x in row:
            if x:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()


if __name__ == '__main__':
    board: Board | None = queens(20)
    if board:
        print_board(board)
    else:
        print('No solution found')
