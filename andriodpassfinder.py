# Generate and print all valid Android-style 3x3 pattern paths

# Rules:
# - Dots numbered 1–9:
#   1 2 3
#   4 5 6
#   7 8 9
# - Can't skip over a dot unless the middle dot is already used.

MIDDLE = {
    (1, 3): 2, (3, 1): 2,
    (1, 7): 4, (7, 1): 4,
    (3, 9): 6, (9, 3): 6,
    (7, 9): 8, (9, 7): 8,
    (1, 9): 5, (9, 1): 5,
    (3, 7): 5, (7, 3): 5,
    (4, 6): 5, (6, 4): 5,
    (2, 8): 5, (8, 2): 5
}

def is_valid(a, b, used):
    """Check if the move a → b is allowed."""
    if (a, b) in MIDDLE:
        return MIDDLE[(a, b)] in used
    return True

def dfs(current, used, path, results):
    results.append(path[:])  # Save every pattern
    for nxt in range(1, 10):
        if nxt not in used and is_valid(current, nxt, used):
            dfs(nxt, used | {nxt}, path + [nxt], results)

def generate_all_patterns():
    all_patterns = []
    for start in range(1, 10):
        dfs(start, {start}, [start], all_patterns)
    return all_patterns

patterns = generate_all_patterns()

print("Total patterns:", len(patterns))
print("------------------------------")

# Print *every* pattern
for p in patterns:
    print(p)
