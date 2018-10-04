//
// Created by Rebecca Chow on 02/10/2018.
//

#include <iostream>
#include <string>

//Function Declarations
void getUserInputs(std::string* input, int* length);
void insertPercent20(char* input, int length);

int main(int argc, char* argv[]){
    //std::string str1;
    //int length;

    //getUserInputs(&str1, &length);
    char input[20] = "My John Msith";
    int length = 13;
    insertPercent20(input, length);

    std::cout << input << std::endl;
    //std::cout << str1 << std::endl;
    //std::cout << str1[1] << std::endl;



    return EXIT_SUCCESS;
}

void getUserInputs(std::string* input, int* length) {
    std::cout << "Give a string: ";
    std::getline(std::cin, *input);
    std::cout << "Give true length of the string: ";
    std::cin >> *length;
}

void insertPercent20(char* input, int length) {
    int space_cnt = 0;

    //find white spaces
    for(int i = 0; i < length; i++) {
        if( input[i] == ' ') {
            space_cnt++;
            std::cout << space_cnt << std::endl;
        }
    }

    //replace with %20
    if( space_cnt != 0) {
        //work backwards so no afraid of overriding values
        int end = length + 2 * space_cnt; //for null char
        for(int i = length - 1; i >= 0 ; i--) {
            if(input[i] == ' ') {
                input[i] = '%';
                input[i+1] = '2';
                input[i+2] = '0';
            }
            else {
                input[i + 2 * space_cnt] = input[i];
            }
        }

        input[end] = '\0';
    }
    std::cout << input << std::endl;

}