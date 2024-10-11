# i in range removes 1 iter

def check_isbn(isbn):
    counter = 0
    multiply_factor = 10

    if 'X' in isbn:
        counter += 10
        for i in range (0, len(isbn)-1):
            counter += int(isbn[i]) * multiply_factor
            multiply_factor -= 1


    else:
        for i in range (0, len(isbn)): 
            counter += int(isbn[i]) * multiply_factor
            multiply_factor -= 1


    if counter % 11 == 0:
        return True
    return False

isbn = input("Enter ISBN: ")
print(check_isbn(isbn))