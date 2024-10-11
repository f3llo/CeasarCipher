stringA = "AAbbA"
stringB = "AAAAA"

def check_any_lowercase(string):
    for i in string:
        if i.islower():
            return True
    return False

print(check_any_lowercase(stringA))
print(check_any_lowercase(stringB))