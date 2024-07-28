def work_on_strings(a,b):
    list1 = list(a)
    list2 = list(b)
    for i in range(len(a)):
        for x in range(len(b)):
            if list1[i].upper() == list2[x] or  list1[i].lower() == list2[x]:
                list2[x] = list2[x].swapcase()
        
    for x in range(len(b)):
        for i in range(len(a)):
            if list2[x].upper() == list1[i] or list2[x].lower() == list1[i]:
                list1[i] = list1[i].swapcase()
    return "".join(list1 + list2)


