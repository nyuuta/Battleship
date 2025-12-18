import pandas as pd
from src.utils import inside, neighbors

SHIP_SIZES = [4,3,3,2,2,2,1,1,1,1]

def read_player_ships():
    ships = []
    occupied = set()

    print("Board size: 10x10")
    print("Coordinates are from 1 to 10")

    for size in SHIP_SIZES:
        while True:
            try:
                if size == 1:
                    raw = input("Ship of size 1 (x y): ").split()
                    if len(raw) != 2:
                        print("Error: enter exactly two numbers")
                        continue
                    x = int(raw[0]) - 1
                    y = int(raw[1]) - 1
                    cells = [(x, y)]
                else:
                    raw = input(f"Ship of size {size} (x1 y1 x2 y2): ").split()
                    if len(raw) != 4:
                        print("Error: enter exactly four numbers")
                        continue
                    x1,y1,x2,y2 = [int(v)-1 for v in raw]
                    cells = []

                    if x1 == x2:
                        step = 1 if y2 >= y1 else -1
                        for y in range(y1, y2+step, step):
                            cells.append((x1,y))
                    elif y1 == y2:
                        step = 1 if x2 >= x1 else -1
                        for x in range(x1, x2+step, step):
                            cells.append((x,y1))
                    else:
                        print("Error: ship must be horizontal or vertical")
                        continue

                if len(cells) != size:
                    print("Error: wrong ship length")
                    continue

                error = False
                for x,y in cells:
                    if not inside(x,y):
                        print("Error: ship goes outside the board")
                        error = True
                    if (x,y) in occupied:
                        print("Error: ships overlap")
                        error = True
                    for nx,ny in neighbors(x,y):
                        if (nx,ny) in occupied:
                            print("Error: ships touch each other")
                            error = True

                if error:
                    continue

                for c in cells:
                    occupied.add(c)
                ships.append(cells)
                break
            except:
                print("Error: invalid input")

    rows = []
    for i, ship in enumerate(ships):
        for x,y in ship:
            rows.append({"ship": i, "x": x, "y": y})

    pd.DataFrame(rows).to_csv("data/player_ships.csv", index=False)
    print("Player ships saved")
