def find_largest_subset_with_sum_limit(s, limit):
    from itertools import combinations 
    s = list(s)
    best_subset = set()
    for r in range(1, len(s) + 1):
        for subset in combinations(s, r):
            if sum(subset) <= limit:
                if len(subset) > len(best_subset):
                    best_subset = set(subset)
    
    return best_subset
n = int(input().strip())
s = set(map(int, input().strip()[1:-1].split(', ')))
limit = int(input().strip())
result = find_largest_subset_with_sum_limit(s, limit)

print(result)