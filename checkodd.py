def check_odd(num):

    for i in range (0, len(num)):
        if (int(num[i]) % 2) != 0:
            return False
    return True


num = input("Enter number")
result = check_odd(num)
print(result)