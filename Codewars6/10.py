def distance(word1, word2):
    operations = 0
    num1 = 0
    num2 = 0

    while num1 < len(word1) or num2 < len(word2):
        if num1 < len(word1) and num2 < len(word2) and word1[num1] == word2[num2]:
            num1 += 1
            num2 += 1
        else:
            operations += 1
            if num1 == len(word1):
                num2 += 1
            elif num2 == len(word2):
                num1 += 1
            else:
                num1 += 1
                num2 += 1

    return operations

print(distance("intention", "execution"))
print(distance("kitten", "sitting"))
