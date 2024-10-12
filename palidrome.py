#palidrome checker

def is_pal_recursion(st, s, e): #recursion

    if st == 0:
        return True
    if st[s] != st[e]:
        return False
    if s < e + 1: # if there is still a substring -> start x < end x + 2 
        return is_pal_recursion(st, s + 1, e + 1)
    
    return True

def is_pal_reverse(st):
    if st.reverse() == st: #builtin func
        return True
    return False

string = input("Enter string: ")
result = is_pal_recursion(string, 0, len(string)-1)
print(result)