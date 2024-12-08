def find_intersection(lists1,lists2):
    lists = []
    for i in lists1:
        if i in lists2 and i not in lists:
            lists.append(i)
    
    return lists

print(find_intersection([1, 2, 3], [2, 3, 4]))
print(find_intersection([1, 1, 2],[1, 3]))