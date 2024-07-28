def smaller(arr):
    lists = []
    for i in range(len(arr)):
        lists.append(sum([1 for x in arr[i:] if x < arr[i]]))
    return lists

