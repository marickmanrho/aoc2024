from itertools import islice


def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def optimize_machine(machine, coins=(3, 1)):
    # Integer programming
    # Solve Qx^T = P
    # Where Q = [[A],[B]], x=[i,j]
    # While minimizing i+3j
    # And i <= 100, j <=100

    # i*ax + j*bx = px
    # i*ay + j*by = py
    # i = (py - j*by)/ay
    # ax*(py-j*by)/ay + j*bx = px
    # ax*py/ay - j *ax*by/ay + j*bx = px
    # j(bx-ax*by/ay) = px - ax*py/ay
    # j = (px-ax*py/ay)/(bx-ax*by/ay)

    ax, ay = machine["A"]
    bx, by = machine["B"]
    px, py = machine["Prize"]
    j = (px - ax * py / ay) / (bx - ax * by / ay)
    i = (py - j * by) / ay

    # Make sure i, and j are integer
    i = round(i)
    j = round(j)

    # Check if solution
    if i * ax + j * bx == px and i * ay + j * by == py:
        if ax % bx == 0 and ay % by == 0:
            if ax / bx == ay / by:
                factor = ax / bx
                # If a is 3x or more times larger than b, then we prefer to use the A button
                if factor > coins[0] / coins[1]:
                    print("-----", i, j)
                    i = i + j % factor
                    j = j // factor
        cost = coins[0] * i + coins[1] * j
    else:
        cost = -1
    return int(cost)


def main():
    offset = 10_000_000_000_000
    machines = []
    with open("day13/input.txt", "r", encoding="utf-8") as f:
        for machine_input in batched(f.readlines(), n=4):
            A, B, Prize = machine_input[:3]
            _, _, ax, ay = A.split(" ")
            _, _, bx, by = B.split(" ")
            _, px, py = Prize.split(" ")
            ax, ay = int(ax.replace("X+", "").replace(",", "")), int(
                ay.replace("Y+", "")
            )
            bx, by = int(bx.replace("X+", "").replace(",", "")), int(
                by.replace("Y+", "")
            )
            px, py = int(px.replace("X=", "").replace(",", "")), int(
                py.replace("Y=", "")
            )

            machines.append(
                {"A": (ax, ay), "B": (bx, by), "Prize": (px + offset, py + offset)}
            )

    required_tokens = [optimize_machine(machine) for machine in machines]
    optimal_tokens = [t for t in required_tokens if t != -1]
    print(f"Solution: {sum(optimal_tokens)}")


if __name__ == "__main__":
    main()
