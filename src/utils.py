BOARD_SIZE = 10

def inside(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                nx, ny = x + dx, y + dy
                if inside(nx, ny):
                    yield nx, ny

def print_board(board, title):
    print(title)
    print("  " + " ".join(str(i+1) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(str(i+1).rjust(2), " ".join(row))
    print()
