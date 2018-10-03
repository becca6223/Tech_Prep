//
// Created by Rebecca Chow on 02/10/2018.
//

#include <iostream>
#include <string>

//Function Declarations
void getUserInputs(std::string* input, int* length);
void insertPercent20(std::string* input, int length);

int main(int argc, char* argv[]){
    std::string str1;
    int length;
    getUserInputs(&str1, &length);




    return EXIT_SUCCESS;
}

void getUserinputs(std::string* input, int* length) {
    std::cout << "Give a string: ";
    std::cin >> *input;
    std::cout << "Give true length of the string: ";
    std::cin >> *length;
}

void insertPercent20(std::string* input, int length) {
    int spacePos[length];
    int j = 0;

    //find white spaces
    for(int i = 0; i < length; i++) {
        if(input[i] == " ") {
            spacePos[j] = 1;
            j++;
        }
    }

    std::string percent = "%20";
    //replace with %20
    if( j != 0) {
        //work backwards so no afraid of overriding values
        int start = spacePos[j-1];
        int end = length;
        for(int i = j - 1; i >= 0; i--) {

        }
    }
}