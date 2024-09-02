def encode(st):
    lists = []
    dict1 = {
        "a": "1",
        "e": "2",
        "i": "3",
        "o": "4",
        "u": "5"
}
    for i in st:
        if i in dict1:
            lists.append(dict1[i])
        else:
            lists.append(i)
    return "".join(lists)
    
    
def decode(st):
    lists = []
    dict1 = {
        "1": "a",
        "2": "e",
        "3": "i",
        "4": "o",
        "5": "u"
}
    for i in st:
        if i in dict1:
            lists.append(dict1[i])
        else:
            lists.append(i)
    return "".join(lists)