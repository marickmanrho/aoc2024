from itertools import product


def traverse_grid(n_rows, n_cols, max_iterations, direction, x, y, obstacles):
    visited_squares = set()
    visited_squares_directional = set()

    # Mapping indicating which directions to move in and take upon hitting an obstacle
    dir_map = {
        "up": {"target": (-1, 0), "next": "right"},
        "right": {"target": (0, 1), "next": "down"},
        "down": {"target": (1, 0), "next": "left"},
        "left": {"target": (0, -1), "next": "up"},
    }

    # While in bounds and within max_iterations
    itt = 0
    while 0 <= x < n_rows and 0 <= y < n_cols and itt < max_iterations:
        # Record visited square
        visited_squares.add((x, y))

        if (x, y, direction) in visited_squares_directional:
            raise ValueError("Found loop")
        else:
            visited_squares_directional.add((x, y, direction))

        # Get target square
        t = dir_map[direction]["target"]
        target = (x + t[0], y + t[1])

        # Assess if target is accessible
        if target in obstacles:
            direction = dir_map[direction]["next"]
        else:
            x, y = target

        itt += 1

    if itt == max_iterations:
        raise RecursionError("Maximum number of iterations reached")

    return visited_squares


def main():
    with open("day6/input.txt", "r", encoding="utf-8") as f:
        grid = [line.strip() for line in f.readlines()]

    # Size of grid
    n_rows = len(grid)
    n_cols = len(grid[0])

    # find guard and obstacles
    guard_position = (0, 0)
    obstacles = []
    for i, j in product(range(n_rows), range(n_cols)):
        if grid[i][j] == "^":
            guard_position = (i, j)
        elif grid[i][j] == "#":
            obstacles.append((i, j))

    # Traverse grid
    x, y = guard_position
    direction = "up"
    max_iterations = 10_000

    # Part 1
    visited_squares = traverse_grid(
        n_rows, n_cols, max_iterations, direction, x, y, obstacles
    )

    print(len(visited_squares))
    # 964 is too low

    # Part 2
    loop_obstacles = []
    for visited_square in visited_squares:
        x, y = guard_position
        direction = "up"
        max_iterations = 10_000
        if visited_square == guard_position:
            continue

        if visited_square in obstacles:
            raise ValueError("Visited square in Obstacle list!")

        _obstacles = obstacles + [visited_square]

        try:
            traverse_grid(n_rows, n_cols, max_iterations, direction, x, y, _obstacles)
        except ValueError:
            loop_obstacles += [visited_square]

    print(len(loop_obstacles))
    # 380 too low
    # 9962 too high


if __name__ == "__main__":
    main()
