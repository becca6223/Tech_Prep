#include <iostream>

//Function Declarations
bool rotateMatrix(int** matrix, int n);
int** initializeMatrix(int n);

int main() {
    int** matrix = initializeMatrix(4);
    bool result  = rotateMatrix(matrix, 4);

    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

//Function Definitions
int** initializeMatrix(int n ) {
    int k = 0;
    int** matrix = (int**) malloc(sizeof(*matrix) * n);
    //std::cout << sizeof(*matrix) * n << std::endl;
    for(int i = 0; i < n; i++) {
        matrix[i] = (int*) malloc(sizeof(*matrix[i]) * n);
        for(int j = 0; j < n; j++) {
            matrix[i][j] = k;
            k++;
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return matrix;
}

bool rotateMatrix(int** matrix, int n) {
    //assume the matrix is n by n
    int layer = n / 2;
    int last = n - 1;


    for(int i = 0; i < layer; i++) {
        int offset1 = 0 ;
        int offset2 = last - 1;
        for(int j = i ; j < last; j ++) {
            int top = matrix[i][j];
            matrix[i][j] = matrix[i + offset2][j - offset1];
            matrix[i + offset2][j - offset1] =  matrix[i + offset2 + offset1][j - offset1 + offset2];
            matrix[i + offset2 + offset1][j - offset1 + offset2] = matrix[i + offset1][j + offset2];
            matrix[i + offset1][j + offset2] = top;

            offset1++;
            offset2--;
        }
        last--;
    }

    return true;
}