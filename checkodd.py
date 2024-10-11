

def check_odd(num):
    num_string = str(num)

    for i in range (0, len(num_string)):
        if (int(num_string[i]) % 2) != 0:
            return False
    return True

num = int(input("Enter number"))
result = check_odd(num)
print(result)