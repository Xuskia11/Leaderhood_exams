def distance(word1, word2):
    word1 = list(word1)
    for i in word2:
        if i in word1:
            word1.remove(i)
    return len(word1) + 1

print(distance("horse", "ros"))
print(distance("intention", "execution"))
print(distance("kitten", "sitting"))
