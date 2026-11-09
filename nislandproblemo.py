def print_board(board):
    for row in board:
        print(" ".join(row))

def solve_n_islands(grid):
    board = [["-" for i in range(n)] for i in range(n)]
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
            board[r][c] = "I"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            board[r][c] = "-"
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return solutions

n = int(input("Enter one lenght of the sea as its square: "))
solutions = solve_n_islands(n)

print(len(solutions))
print(f"One of {len(solutions)} solutions:")
print_board(solutions[0])
print("They cant attack each other as they arent connected by the safest routes(which are the lines) from all sides diagnol front back left and right so they are all safe from each other and they also wont risk a harder route top attack.")