with open('input.txt', 'r') as f:
    lines = f.readlines()

num_valid = 0

# split string into usable pieces
for line in lines:
    splits = line.split(" ")

    # split bounds into min max
    min_max = splits[0]
    # no concept of index 0, subtract 1!
    pos1, pos2 = [int(i) - 1  for i in min_max.split("-")]

    # remove : from letter
    letter = splits[1][0]

    # determine password validity
    # index into string
    pswd = splits[2]

    if (pswd[pos1] == letter) is not (pswd[pos2] == letter):
        num_valid += 1

print(num_valid)
