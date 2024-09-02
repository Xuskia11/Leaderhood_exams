def is_divisible(*num):
    word = True
    for i in num[1:]:
        if num[0] % i == 0:
            word = True
        else:
            word = False
            if word == False:
                return word
    return word
