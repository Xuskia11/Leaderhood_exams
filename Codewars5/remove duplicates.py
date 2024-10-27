# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']


def remove(lists):
    listn = []
    for i in lists:
        if i not in listn:
            listn.append(i)
    return listn

print(remove(['a', 'b', 'a', 'c']))