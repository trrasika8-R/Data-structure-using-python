from itertools import combinations
list = [-1,9, 10, -3, 2]
print("Positive Combinations")
for r in range(1, len(list)+1):
    for combo in combinations(list, r):
        if all(num>0 for num in combo):
            print(combo)
