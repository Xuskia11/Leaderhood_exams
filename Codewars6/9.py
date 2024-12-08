def prime(start,end):
    lists = []
    for i in range(start, end + 1):
        if i == 1:
            lists.append(i)
        elif i > 1:
            is_prime = True
            for num in range(2,i):
                if i % num == 0:
                    is_prime = False
                    break
            if not is_prime:
                lists.append(i)

    return lists
            


print(prime(10,20))
print(prime(1,10))
print(prime(20,30))