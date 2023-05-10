import random

for i in range(0, 101):
    filename = "Input-P" + str(i) + "-0"
    permutation = random.sample([1, 2, 3, 4], 4)
    with open(filename, "w") as f:
        for num in permutation:
            f.write(str(num) + " ")
