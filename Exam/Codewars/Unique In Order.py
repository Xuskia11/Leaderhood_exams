def unique_in_order(sequence):
    if not sequence:
        return []
    elif len(sequence) == 1:
        return list(sequence)
    else:
        lists = []
        for i in range(len(sequence) - 1):
            if sequence[i] != sequence[i + 1]:
                lists.append(sequence[i])
            
        lists.append(sequence[-1])
        return lists