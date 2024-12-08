def sums(lists):
    num = 0
    for i in lists:
        if i > 0:
            num += i
        elif i == None:
            return 0
    return num

print(sums([1, -4, 7, 12]))
print(sums([-1, -2, -3, -4]))
print(sums([]))