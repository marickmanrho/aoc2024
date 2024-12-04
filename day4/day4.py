def part_1():
    word = "XMAS"

    grid = []
    with open('day4/input.txt', 'r') as f:
        for line in f.readlines():
            grid.append([i for i in line])

    n_rows = len(grid)
    n_cols = len(grid[0])

    # Pad the grid with 4x"." to allow the window to fit always
    Nword = 0

    # Go over all grid positions
    for row, line in enumerate(grid):
        for col, val in enumerate(line):
            if val == "X":
                for up_down in [1,0,-1]:
                    for left_right in [1,0,-1]:
                        if up_down==0 and left_right==0:
                            continue
                        c = 1
                        for x, letter in enumerate(word[1:], 1):
                            letter_row = row + up_down*x
                            col_offset = col + left_right*x

                            if letter_row >= n_rows or letter_row < 0:
                                continue
                            if col_offset >= n_cols or col_offset < 0:
                                continue

                            if grid[letter_row][col_offset] == letter:
                                c +=1
                            else:
                                break
                        if c == len(word):
                            Nword += 1
    
    print(Nword)
    # 2415 is too high

def part_2():
    grid = []
    with open('day4/input.txt', 'r') as f:
        for line in f.readlines():
            grid.append([i for i in line])

    Nword = 0

    # Go over all grid positions
    positions = [(-1,1),(-1,-1),(1,-1),(1,1)]
    letters = "MMSS"
    for row, line in enumerate(grid[1:-1],1):
        for col, val in enumerate(line[1:-1],1):
            if val == "A":
                for rotation in range(len(positions)):

                    for i, letter in enumerate(letters):
                        p = i+rotation
                        if p>=len(positions):
                            p -= len(positions)

                        x,y = positions[p]
                        if grid[row+x][col+y] != letter:
                            break
                    
                        if i == len(letters)-1:
                            Nword+=1


    print(Nword)
    # 431 is too low

if __name__=="__main__":
    part_1()
    part_2()