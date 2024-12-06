def main():
    with open("day2/input.txt", "r", encoding="utf-8") as f:
        reports = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]

    num_invalid_reports = 0
    for report in reports:
        n_possible_dampened_reports = len(report) + 1
        num_invalid_dampened_reports = 0

        dampened_reports = [report]
        for skip_index in range(len(report)):
            dampened_report = [x for i, x in enumerate(report) if i != skip_index]
            dampened_reports.append(dampened_report)

        for dampened_report in dampened_reports:
            x1 = dampened_report[0]
            x2 = dampened_report[1]

            if abs(x1 - x2) > 3 or abs(x1 - x2) == 0:
                num_invalid_dampened_reports += 1
                continue
            if x1 > x2:
                x1 = x2
                for x2 in dampened_report[2:]:
                    if x1 - x2 > 3 or x1 - x2 < 1:
                        num_invalid_dampened_reports += 1
                        break
                    x1 = x2
            elif x1 < x2:
                x1 = x2
                for x2 in dampened_report[2:]:
                    if x1 - x2 < -3 or x1 - x2 > -1:
                        num_invalid_dampened_reports += 1
                        break
                    x1 = x2

        if n_possible_dampened_reports == num_invalid_dampened_reports:
            num_invalid_reports += 1

    print(f"Number of valid reports = {len(reports)-num_invalid_reports}")


if __name__ == "__main__":
    main()
