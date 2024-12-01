import logging
import numpy as np

logger = logging.getLogger()

def main():
    # Empty lists to read content into
    l1, l2 = [], []
    with open('day1\input.txt', 'r') as f:
        for line in f.readlines():
            n1, n2 = line.split(' '*3)
            l1.append(int(n1))
            l2.append(int(n2))
    
    # Sort both lists
    l1.sort()
    l2.sort()

    # Compute distances between each pair of numbers
    dif = np.array(l1)-np.array(l2)

    # Solution part 1
    logger.info(f"Sum of differences is {np.sum(np.abs(dif))}")

    # Compute a list of IDs that may exist, those will be the bins
    # of our histogram
    min_id = min(l1+l2)
    max_id = max(l1+l2)
    logger.debug(f"{min_id=}")
    logger.debug(f"{max_id=}")
    
    bins = np.arange(min_id, max_id+2, 1)

    # Compute histogram of both lists
    hist_l1, _ = np.histogram(l1, bins=bins)
    hist_l2, _ = np.histogram(l2, bins=bins)

    logger.debug(f"length of l1 {len(l1)} ?= {hist_l1.sum()}")
    logger.debug(f"length of l2 {len(l2)} ?= {hist_l2.sum()}")

    # Solution part 2
    # Similarity score is the ID times the number of times that ID occurs in list 1 
    # times the number of times it occurs in list 2
    logger.info(f"Similarity score is {np.sum(bins[:-1]*hist_l1*hist_l2)}")

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()