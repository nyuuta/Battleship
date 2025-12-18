import random
import pandas as pd
from src.utils import inside, neighbors

SHIP_SIZES = [4,3,3,2,2,2,1,1,1,1]

def generate_bot_ships():
    occupied = set()
    ships = []

    for size in SHIP_SIZES:
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9)
            dx, dy = random.choice([(1,0),(0,1)])

            cells = [(x + i*dx, y + i*dy) for i in range(size)]

            ok = True
            for c in cells:
                if not inside(*c) or c in occupied:
                    ok = False
                for n in neighbors(*c):
                    if n in occupied:
                        ok = False

            if not ok:
                continue

            for c in cells:
                occupied.add(c)
            ships.append(cells)
            break

    rows = []
    for i, ship in enumerate(ships):
        for x,y in ship:
            rows.append({"ship": i, "x": x, "y": y})

    pd.DataFrame(rows).to_csv("data/bot_ships.csv", index=False)
