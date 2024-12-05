from itertools import combinations

def put_in_correct_order(update, page_ordering_rules, idx=0):
    if idx == len(update)-1:
        return update
    
    for i in range(idx+1,len(update)):
        if (update[i], update[idx]) in page_ordering_rules:
            u = [x for x in update]
            u.pop(idx)
            u.append(update[idx])
            
            return put_in_correct_order(u, page_ordering_rules, idx=idx)
    
    return put_in_correct_order(update, page_ordering_rules, idx=idx+1)


def main():
    page_ordering_rules = []
    with open('day5/input.txt', 'r') as f:
        line = f.readline()
        while line.strip()!="":
            ordering_rule = tuple(map(int, line.strip().split('|')))
            page_ordering_rules.append(ordering_rule)
            line = f.readline()
        
        updates = [list(map(int,line.strip().split(','))) for line in f.readlines()]

    correct_ordered_sum = 0
    incorrect_ordered_sum = 0
    for update in updates:
        for x,y in combinations(update, 2):
            if (y,x) in page_ordering_rules:
                u = put_in_correct_order(update, page_ordering_rules)
                idx = int((len(u)-1)/2)
                incorrect_ordered_sum += u[idx]
                break
        else:
            idx = int((len(update)-1)/2)
            correct_ordered_sum += update[idx]
    
    print(f"Answer part 1: {correct_ordered_sum}")
    # 530457 is too high

    print(f"Answer part 2: {incorrect_ordered_sum}")
    # 4819 is too high

if __name__=="__main__":
    main()