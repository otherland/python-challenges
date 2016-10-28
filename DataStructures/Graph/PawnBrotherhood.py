"""
You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns.

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

"""

"""
If pawn has a sister in row[-1][col-1] or row[-1][col+1], pawn is safe
"""
checkio = lambda board : sum(
    any((chr(ord(pawn[0])+i) + str(int(pawn[1])-1) in board) for i in (-1, 1)) for pawn in board
    )

# checkio = lambda board : [
#     (chr(ord(pawn[0])+1) + str(int(pawn[1])-1),
#     chr(ord(pawn[0])-1) + str(int(pawn[1])-1))
#     for pawn in board]

print(checkio({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(checkio({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))