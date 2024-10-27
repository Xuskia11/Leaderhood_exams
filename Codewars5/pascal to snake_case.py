# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"


def convert(word):
    cases = ""
    for i in word:
        if i.isupper() and cases:
            cases += "_"
        cases += i.lower()
    return cases

print(convert("TestController"))
