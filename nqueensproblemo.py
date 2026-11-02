# N queens: print total solutions and show one solution

def print_board(board):
    for row in board:
        print(" ".join(row))

def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    cols = set()
    diag1 = set() # r - c
    diag2 = set() # r + c
    solutions = []

    def backtrack(r):
        if r == n:
            solutions.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return solutions

# Drivers code
n = 4
solutions = solve_n_queens(n)

print(len(solutions))
print(f"One of {len(solutions)} solutions:")
print_board(solutions[0])