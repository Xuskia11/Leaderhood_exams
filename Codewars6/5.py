def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    
    for i in set(str1):
        if str1.count(i) != str2.count(i):
            return False
    return True

print(anagram("listen", "silent"))
print(anagram("hello", "world"))
print(anagram("triangle", "integral"))