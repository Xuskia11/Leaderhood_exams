def longest_substring(str):
    sub = []
    num = 0
    for i in str:
        if i in sub:
            while i in sub:
                sub.pop(0)

        sub.append(i)
        num = max(num, len(sub))
    return num

print(longest_substring(("pwwkew")))

