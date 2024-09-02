def cakes(recipe, available):
    lists = []
    for i in recipe:
        if i in available:
            lists.append(available[i] // recipe[i])
        else:
            return 0
    return min(lists)