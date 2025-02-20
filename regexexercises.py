import re

# Exercise 1: program to check that a string contains 
# only a certains et of characters (a-z, A-Z, 0-9)

def check_string(string):
    regex = re.compile(r'[a-zA-Z0-9] [*&%@#!}{]')
    match = regex.search(string)
    match = re.split('\s',string)
    print(match)
    return bool(match)

print(check_string("ABCD EF ab cde f12 3450"))
print(check_string("*&%@#!}{"))


# Exercise 2: program that matches a string that has an a
# followed by 0 or more b's
def ex_five(string):
    regex = re.compile('a(b*)$')
    if regex.search(string):
        return (f'Found a match: {string}')
    else:
        return (f'Match not found: {string}')
    

print(ex_five("ac"))
print(ex_five("abc"))
print(ex_five("a"))
print(ex_five("ab"))
print(ex_five("ab"))

print("-------------------------------")
print("\n\n\nExercise 3\n")

# Exercise 3: program that matches a string that
# has an a followed by one or more b's
def ex_five(string):
    regex = re.compile('ab+?')
    if regex.search(string):
        return (f'Found a match: {string}')
    else:
        return (f'Match not found: {string}')

print(ex_five("ac"))
print(ex_five("abc"))
print(ex_five("a"))
print(ex_five("ab"))
print(ex_five("aabb"))
print("-------------------------------\n\n\n")

print("Exercise 4\n")
# Exercise 4: program matches string that has an a
# followed by zero or one b

def ex_five(string):
    regex = re.compile('ab?')
    if regex.search(string):
        return (f'Found a match: {string}')
    else:
        return (f'Match not found: {string}')

print(ex_five("ac"))
print(ex_five("abc"))
print(ex_five("a"))
print(ex_five("ab"))
print(ex_five("abb"))
print(ex_five("babbbb"))
print("-------------------------------\n\n\n")


print("Exercise 5\n")
# program matches a string that has an a
# followed by three bs
def ex_five(string):
    regex = re.compile(r'ab{2,3}?')
    if regex.search(string):
        return (f'Found a match: {string}')
    else:
        return (f'Match not found: {string}')
    
print(ex_five("ac"))
print(ex_five("abc"))
print(ex_five("a"))
print(ex_five("ab"))
print(ex_five("abb"))
print(ex_five("babbb baa abbb"))
print("-------------------------------\n\n\n")