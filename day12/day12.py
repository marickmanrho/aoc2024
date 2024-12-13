from itertools import product


def get_area(start: tuple, plots: set[tuple], grid: list[list[str]], area: set[tuple]):
    area.add(start)
    x, y = start
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for neighbor in neighbors:
        if neighbor in plots:
            nx, ny = neighbor
            if grid[x][y] == grid[nx][ny]:
                plots.remove(neighbor)
                area.add(neighbor)
                plots, area = get_area(neighbor, plots, grid, area)

    return plots, area


def main():
    with open("day12/input.txt", "r", encoding="utf-8") as f:
        grid = [line.strip() for line in f.readlines()]

    grid_size = (len(grid), len(grid[0]))
    plots = {(i, j) for i, j in product(range(grid_size[0]), range(grid_size[1]))}

    areas = []
    while plots:
        start = plots.pop()
        plots, area = get_area(start, plots, grid, set())
        areas.append(area)

    costs = []
    bulk_costs = []
    for area in areas:
        border = set()
        for plot in area:
            x, y = plot
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for neighbor in neighbors:
                if (neighbor, plot) in border:
                    border.remove((neighbor, plot))
                else:
                    border.add((plot, neighbor))

        costs.append(len(area) * len(border))

        nodes = []
        for edge in border:
            plot, neighbor = edge
            right = ((plot[0], plot[1] + 1), (neighbor[0], neighbor[1] + 1))
            down = ((plot[0] + 1, plot[1]), (neighbor[0] + 1, neighbor[1]))
            if right not in border and down not in border:
                nodes.append(edge)
        bulk_costs.append(len(area) * len(nodes))

    print(f"Solution part 1: {sum(costs)}")
    print(f"Solution part 2: {sum(bulk_costs)}")


if __name__ == "__main__":
    main()
