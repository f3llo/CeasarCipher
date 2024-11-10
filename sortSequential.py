
def find_element(array, e):
    for i in array:
        if i == e:
            return True
    return False

def binary_search(array, s, e, v): #sorted array
    #mid -1
    mid = (s+e) // 2
    if s == e - 1:
        return False
    elif v == array[mid]:
        return mid #index
    elif v > array[mid]:
        return binary_search(array, mid+1, e, v)
    elif v < array[mid]:
        return binary_search(array, s, mid-1, v)

array = [5,11,13,20,25,27,35]
print(binary_search(array, 0, 7, 26))


