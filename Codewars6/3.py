def missing_number(lists):
    n = len(lists) + 1
    sum1 = n * (n + 1) // 2
    sum2 = sum(lists)
    return sum1 - sum2

print(missing_number([1, 2, 4, 5]))