#include<iostream>
using namespace std;

int main() {
    int matrix[10][10]; // declaring matix 10 x 10.
    /* input elements ex:
     * 1 2 3
     * 4 5 6
     * 7 8 9
     * this example contains 3 rows and 3 columns. */
    cout << "Enter matrix elements (10x10):" << endl;
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            cin >> matrix[i][j];
        }
    }

    // find maximum element in the matrix
    int max = matrix[0][0]; // set the first element as max.
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            if(matrix[i][j] > max) {
                max = matrix[i][j];
            }
        }
    }
    cout << "Maximum element in the matrix: " << max << endl;

    // find maximum element in each row and print.
    for(int i = 0; i < 10; i++) {
        max = matrix[i][0];
        for(int j = 0; j < 10; j++) {
            if(matrix[i][j] > max) {
                max = matrix[i][j];
            }
        }
        cout << "Max element in " << i+1 << "th row is: " << max << endl;
    }

    // find maximum element in each column and print.
    for(int i = 0; i < 10; i++) {
        max = matrix[0][i];
        for(int j = 0; j < 10; j++) {
            if(matrix[j][i] > max) {
                max = matrix[j][i];
            }
        }
        cout << "Max element in " << i + 1 << "th column is: " << max << endl;
    }

    return 0;
}
