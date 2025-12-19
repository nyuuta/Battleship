import pandas as pd
import random
from src.utils import print_board, neighbors, BOARD_SIZE

def load_ships(path):
    df = pd.read_csv(path)
    ships = {}
    for ship_id in df['ship'].unique():
        coords = df[df['ship'] == ship_id][['x','y']].values
        ships[ship_id] = set((x,y) for x,y in coords) 
    return ships


def play_game():
    player_ships = load_ships("data/player_ships.csv")
    bot_ships = load_ships("data/bot_ships.csv")

    player_ship_sizes = {sid: len(cells) for sid, cells in player_ships.items()}
    bot_ship_sizes = {sid: len(cells) for sid, cells in bot_ships.items()}

    player_board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    bot_board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    bot_moves = set()
    turn = 1
    log = []

    while player_ships and bot_ships:
        print(f"\n--- Turn {turn} ---")
        print_board(bot_board, "BOT BOARD")

        while True:
            try:
                move = input("Your move x y (1-10): ").split()
                if len(move) != 2:
                    print("Enter exactly two numbers")
                    continue
                x, y = int(move[0])-1, int(move[1])-1
                if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
                    print("Coordinates out of board")
                    continue
                if bot_board[y][x] in ["X","o"]:
                    print("Cell already targeted")
                    continue
                break
            except:
                print("Invalid input, try again")

        hit = False
        for sid in list(bot_ships.keys()):
            if (x,y) in bot_ships[sid]:
                hit = True
                bot_board[y][x] = "X"
                bot_ships[sid].remove((x,y))
                if not bot_ships[sid]:
                    print(f"You destroyed a ship of size {bot_ship_sizes[sid]}")
                    for cx,cy in neighbors(x,y):
                        if bot_board[cy][cx] == ".":
                            bot_board[cy][cx] = "o"
                    del bot_ships[sid]
                break
        if not hit:
            bot_board[y][x] = "o"

        while True:
            bx, by = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
            if (bx,by) not in bot_moves:
                bot_moves.add((bx,by))
                break

        bhit = False
        for sid in list(player_ships.keys()):
            if (bx,by) in player_ships[sid]:
                bhit = True
                player_board[by][bx] = "X"
                player_ships[sid].remove((bx,by))
                if not player_ships[sid]:
                    print(f"Bot destroyed your ship of size {player_ship_sizes[sid]}")
                    for cx,cy in neighbors(bx,by):
                        if player_board[cy][cx] == ".":
                            player_board[cy][cx] = "o"
                    del player_ships[sid]
                break
        if not bhit:
            player_board[by][bx] = "o"

        print_board(player_board, "PLAYER BOARD")

        log.append({
            "turn": turn,
            "player_move": f"{x+1},{y+1}:{'hit' if hit else 'miss'}",
            "bot_move": f"{bx+1},{by+1}:{'hit' if bhit else 'miss'}",
            "player_board": str(player_board),
            "bot_board": str(bot_board)
        })

        pd.DataFrame(log).to_csv("data/game_state.csv", index=False)
        turn += 1

    print("Game over")
    if not player_ships:
        print("Bot wins!")
    else:
        print("You win!")
