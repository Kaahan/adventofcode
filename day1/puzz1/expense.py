with open('input.txt', 'r') as f:
    lines = f.readlines()

vals = [int(line) for line in lines]

# find the expenses that sum to 2020
sums = {}
for i, val in enumerate(vals):
    sums[val] = i

for i, val in enumerate(vals):
    if 2020 - val in sums.keys() and sums[2020 - val] != i:
        print(f"product is {val * (2020 - val)}")
