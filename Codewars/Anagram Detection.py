def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    x = sorted(test)
    y = sorted(original)
    if x == y:
        return True
    return False

