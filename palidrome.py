#palidrome checker

def is_pal(st, s, e):

    if st == 0:
        return True
    if st[s] != st[e]:
        return False
    if s < e + 1: # if there is still a substring
        return is_pal(st, s + 1, e + 1)
    
    return True

string = input("Enter string: ")
result = is_pal(string, 0, len(string)-1)
print(result)