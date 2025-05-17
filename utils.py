import random

def next_gen(live_cells):
    from collections import defaultdict
    neighbor_counts = defaultdict(int)
    for x, y in live_cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    neighbor_counts[(x + dx, y + dy)] += 1
    new_live_cells = set()
    for cell, count in neighbor_counts.items():
        if count == 3 or (count == 2 and cell in live_cells):
            new_live_cells.add(cell)
    return new_live_cells

def random_fill(width, height):
    return {(x, y) for x in range(width) for y in range(height) if random.random() < 0.2}

def save_pattern(live_cells, filename):
    with open(filename, 'w') as f:
        for x, y in live_cells:
            f.write(f"{x},{y}\n")

def load_pattern(filename):
    live_cells = set()
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    x, y = map(int, line.split(','))
                    live_cells.add((x, y))
    except FileNotFoundError:
        pass
    return live_cells
