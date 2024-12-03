import regex as re

def main():
    with open('day3/input.txt', 'r') as f:
        lines = f.readlines()

    pattern_part_1 = r"(mul\(\d{1,3},\d{1,3}\))"
    pattern_part_2 = r"(mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\))"
    pattern = pattern_part_2
    answer = 0

    do = True
    for line in lines:
        matches = re.findall(pattern, line)

        for match in matches:
            if match == 'do()':
                do = True
            elif match == 'don\'t()':
                do = False
            elif do:
                x,y = match[4:-1].split(',')
                answer += int(x)*int(y)
            
    print(answer)

if __name__=="__main__":
    main()