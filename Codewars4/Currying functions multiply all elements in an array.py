def multiply_all(array):
    def multiplyAll(integer):
        lists = []
        for i in array:
            lists.append(i * integer)
        return lists
    return multiplyAll