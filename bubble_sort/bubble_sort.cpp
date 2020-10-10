#include<iostream>

using namespace std;

void bubble_sort(int *array, int size) {
    for(int i = 0; i < size; i++) {
        for(int j = i; j < size; j++) {
            if(array[i] > array[j]) {
                swap(array[i], array[j]);
            }
        }
    }
}

int main() {
    int array[] = {4,2,1,3,45,6};
    int size = sizeof(array)/sizeof(array[0]);
    bubble_sort(array, size);
    for(int i = 0; i < size; i++) {
        cout<<array[i]<<' ';
    }
    cout<<endl;
    return 0;
}
