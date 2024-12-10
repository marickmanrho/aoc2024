def traverse_trails(trail_map, map_size, head, distinct=True, visited=[], score=0):
    x,y = head
    current_level = trail_map[x][y]

    if current_level == 9:
        return score + 1, visited

    directions = []
    if x > 0:
        directions.append((x-1,y))
    if x < map_size[0]-1:
        directions.append((x+1,y))
    if y > 0:
        directions.append((x,y-1))
    if y < map_size[1]-1:
        directions.append((x,y+1))


    for d in directions:
        if distinct and d in visited:
            continue
        if trail_map[d[0]][d[1]] == current_level + 1:
            score, visited = traverse_trails(trail_map, map_size, d, distinct, visited + [d], score=score)
    
    return score, visited


def main():
    with open('day10/input.txt', 'r', encoding='utf-8') as f:
        trail_map = [list(map(int, line.strip())) for line in f.readlines()]
    
    trail_heads = []
    for i, row in enumerate(trail_map):
        for j, val in enumerate(row):
            if val == 0:
                trail_heads.append((i,j))

    map_size = (len(trail_map), len(trail_map[0]))

    trail_head_scores = []
    trail_head_rating = []
    for head in trail_heads:
        score,_ = traverse_trails(trail_map, map_size, head, distinct=True)
        trail_head_scores.append(score)

        rating,_ = traverse_trails(trail_map, map_size, head, distinct=False)
        trail_head_rating.append(rating)


    print(f"Solution part 1 = {sum(trail_head_scores)}")
    print(f"Solution part 2 = {sum(trail_head_rating)}")

if __name__=="__main__":
    main()