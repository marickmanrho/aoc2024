from itertools import combinations


def main():
    antennas = {}
    part_1 = False

    with open("day8/input.txt", "r", encoding="utf-8") as f:
        for i, row in enumerate(f.readlines()):
            for j, char in enumerate(row.strip()):
                grid_size = (i, j)
                if char == ".":
                    continue
                if char not in antennas:
                    antennas[char] = [(i, j)]
                else:
                    antennas[char].append((i, j))

    if part_1:
        min_multiplyer = 1
        max_multiplyer = 2
    else:
        min_multiplyer = 0
        max_multiplyer = grid_size[0]

    anti_nodes = set()
    for values in antennas.values():
        for p1, p2 in combinations(values, r=2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]

            for i in range(min_multiplyer, max_multiplyer):

                an1 = (p1[0] + i * dx, p1[1] + i * dy)
                an2 = (p2[0] - i * dx, p2[1] - i * dy)

                for an in [an1, an2]:
                    if (
                        an[0] >= 0
                        and an[0] <= grid_size[0]
                        and an[1] >= 0
                        and an[1] <= grid_size[1]
                    ):
                        anti_nodes.add(an)

    print(len(anti_nodes))
    # for part 1
    # 159 is too low


if __name__ == "__main__":
    main()
