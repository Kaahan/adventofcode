with open('input.txt', 'r') as f:
    lines = f.readlines()

vals = [int(line) for line in lines]

sums = {}
for i, val in enumerate(vals):
    for j, lav in enumerate(vals):
        sums[val + lav] = (i, j)

for i, val in enumerate(vals):
    if 2020 - val in sums.keys() and i not in sums[2020 - val]:
        f, s = sums[2020 - val]
        print(f"product is {val * vals[f] * vals[s]}")
