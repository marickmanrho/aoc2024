from itertools import chain, accumulate

def part_1(input):
    file_chunks = input[::2]
    file_blocks = list(chain.from_iterable([[idx]*i for idx, i in enumerate(file_chunks)]))

    loose = []
    for i, chunk in enumerate(input):
        if i%2==0:
            for _ in range(chunk):
                if file_blocks:
                    loose.append(file_blocks.pop(0))
        else:
            for _ in range(chunk):
                if file_blocks:
                    loose.append(file_blocks.pop(-1))
    
    return loose


def part_2(input):
    disk_size = sum(input)
    result = [0]*disk_size

    chunk_starts = [0] + list(accumulate(input))

    len_input = len(input)
    # Start with blocks in the back
    for i in reversed(range(0,len_input,2)):
        # Search all empty blocks in front of i
        for j in range(1,i,2):
            # if they fit
            if input[i] <= input[j]:
                # Write result in that position
                result[chunk_starts[j]:chunk_starts[j]+input[i]] = [int(i//2)]*input[i]
                # Update empty space remaining
                input[j] -= input[i]
                # Update start index of empy space
                chunk_starts[j] += input[i]
                break
        else:
            # If no empty block was big enough, write result to original position
            result[chunk_starts[i]:chunk_starts[i]+input[i]] = [int(i//2)]*input[i]

    
    return result

if __name__=="__main__":
    with open('day9/input.txt', 'r', encoding='utf-8') as f:
        input = [int(i) for i in f.readline().strip()]

    loose = part_1(input)
    print("solution part 1 ", sum(i*j for i,j in enumerate(loose)))

    loose = part_2(input)
    print("solution part 2 ", sum(i*j for i,j in enumerate(loose)))
    # 6328478163785 is too low
    # 6335972980679 is correct
    # 7296405354259 is too high

