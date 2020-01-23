def binary_search(array, value):
    low = 0
    high = len(array)
    middle = int(high / 2)
    while high - 1 > low:
        if array[middle] < value:
            low = middle
        elif array[middle] > value:
            high = middle
        else:
            return middle
        middle = int((low + high)/2)
    return -1

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(a, 5))
    test_list = [1,3,9,11,15,19,29]
    print(binary_search(test_list, 15))
    test_list = [1,3,9,11,15,19,29]
    test_val1 = 25
    test_val2 = 15
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))
