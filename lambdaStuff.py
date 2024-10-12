#These do violate PEP 8... sorry

#or slicing (traverse string backwards) + lambda one liner
lambda_check_palidrome = lambda st: True if st[::-1] == st else False

lambda_any_lowercase = lambda st: True if [x.islower() for x in st] == True else False

#this one does not work yet
lambda_check_odd = lambda n: False if [(int(str(n)[x]) % 2) == 0 for x in range(0, len(str(n)))] != True else True

#ultimite lambda power
lambda_check_isbn = lambda isbn, counter = [10,9,8,7,6,5,4,3,2,1]: True if isbn[9] != "X" and ((sum([x for x in int(isbn)] * [i for i in counter]) % 11) == 0) else False 
lambda_check_Xisbn = lambda isbn, counter = [10,9,8,7,6,5,4,3,2,1]: True if isbn[9] == "X" and ((sum([x for x in (int(isbn) - 1)] * [i for i in counter - 1], 10) % 11) == 0) else False

print(lambda_check_odd(33))