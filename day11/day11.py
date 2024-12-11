from functools import cache

@cache
def track_splits(number, blinks=25):
    if blinks == 0:
        return 1
    
    num_size = len(number)
    if num_size%2==0:
        x,y = number[:int(num_size/2)], number[int(num_size/2):]
        x = str(int(x))
        y = str(int(y))
        return track_splits(x, blinks-1) + track_splits(y, blinks-1)
    elif number == "0":
        return track_splits("1", blinks-1)
    else:
        return track_splits(str(int(number)*2024), blinks-1)
    


def main():
    with open('day11/input.txt', 'r', encoding='utf-8') as f:
        numbers = f.readline().strip().split(' ')

    splits = [track_splits(number, blinks=25) for number in numbers]
    print(f"solution part 1: {sum(splits)}")

    splits = [track_splits(number, blinks=75) for number in numbers]
    print(f"solution part 2: {sum(splits)}")


if __name__=="__main__":
    main()