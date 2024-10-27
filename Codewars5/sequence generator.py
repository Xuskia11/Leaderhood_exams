# 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]


def generator(word):
    lists = []
    for i in range(word):
        if i == 0:
            lists.append(0)
        elif i == 1:
            lists.append(1)
        else:
            lists.append(lists[i - 1] + lists[i - 2])
    return lists

print(generator(7))