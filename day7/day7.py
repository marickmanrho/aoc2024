def callibrate(target, numbers, answer):
    if len(numbers) == 0:
        return answer == target
    elif answer > target:
        return False

    next_number = numbers[0]

    if callibrate(target, numbers[1:], answer + next_number):
        return True
    elif callibrate(target, numbers[1:], int(str(answer) + str(next_number))):
        return True
    else:
        return callibrate(target, numbers[1:], answer * next_number)


def main():
    with open("day7/input.txt", "r", encoding="utf-8") as f:
        callibrations = f.readlines()

    solution = 0
    for callibration in callibrations:
        target, *numbers = list(
            map(int, callibration.strip().replace(":", "").split(" "))
        )
        if callibrate(target, numbers[1:], numbers[0]):
            solution += target

    print(solution)

    # For part 2
    # 456567238446228 is too high


if __name__ == "__main__":
    main()
