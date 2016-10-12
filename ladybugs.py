from collections import Counter

def solution(board):
    cells = [0] + [i for i in board if i.isalpha()] + [0]
    c = Counter(cells)
    if any(i < 2 for i in c.values()):
        return "NO"
    for i in range(1, len(cells)-1):
        if (cells[i-1] != cells[i]) and (cells[i] != cells[i+1]):
            if not "_" in board:
                return "NO"
    return "YES"

assert solution("RRBBR_") == "YES"
assert solution("RBY_YBR") == "YES"
assert solution("X_Y__X") == "NO"
assert solution("__") == "YES"
assert solution("B_RRBR") == "YES"
assert solution("RBRB") == "NO"
assert solution("RRRR") == "YES"
assert solution("BBB") == "YES"
assert solution("BBB_") == "YES"
