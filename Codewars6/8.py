def longest_sequence(listn):
    if not listn:
        return 0
    
    set_num = set(listn)
    num = 1
    for i in set_num:
        if i - 1 not in set_num:
            current = num
            current2 = 1
        
        while current + 1 in set_num:
            current += 1
            current2 += 1

        num = max(num,current2)
    return num





print(longest_sequence([100, 4, 200, 1, 3, 2]))
print(longest_sequence([9, 1, 4, 7, 3, 2, 8, 5, 6]))
print(longest_sequence([0, 0]))