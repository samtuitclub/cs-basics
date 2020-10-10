#include<iostream>

using namespace std;

int binary_search(int array[], int low, int hight, int value) {
    if (low > hight) {
        return -1;
    }
    int middle = (low + hight) / 2;
    if(array[middle] < value) {
        return binary_search(array, middle + 1, hight, value);
    } else if (array[middle] > value) {
        return binary_search(array, low, middle - 1, value);
    } else if (array[middle] == value) {
        return middle;
    }

    return -1;
}

int find(int array[], int size, int value) {
    return binary_search(array, 0, size, value);
}

int main() {
    int array1[] = {1,3,4,5,6,7,8,9,10};
    int size = sizeof(array1)/sizeof(array1[0]);
    cout<<find(array1, size, 8)<<endl; // returns 6
    int array2[] = {1,2,4,6,7,8};
    size = sizeof(array2)/sizeof(array2[0]);
    cout<<find(array2, size, 9)<<endl; // returns -1
    return 0;
}
