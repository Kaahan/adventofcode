with open('input.txt', 'r') as f:
    lines = f.readlines()

num_valid = 0

# split string into usable pieces
for line in lines:
    splits = line.split(" ")

    # split bounds into min max
    min_max = splits[0]
    bound = [int(i) for i in min_max.split("-")]

    # remove : from letter
    letter = splits[1][0]

    # determine password validity
    if splits[2].count(letter) in range(bound[0], bound[1] + 1):
        num_valid += 1

print(num_valid)
