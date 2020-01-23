def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key

if __name__ == "__main__":
    a = [2,3,5,2,1,4,6,83,1]
    insertion_sort(a)
    print(a)
