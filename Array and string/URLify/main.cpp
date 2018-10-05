//
// Created by Rebecca Chow on 02/10/2018.
//

#include <iostream>
#include <string>

//Function Declarations
void insertPercent20(char* input, int length);

int main(int argc, char* argv[]){
    char input[20] = "My John Smith";
    int length = 13;

    std::cout << input << std::endl;

    insertPercent20(input, length);

    std::cout << input << std::endl;


    return EXIT_SUCCESS;
}


void insertPercent20(char* input, int length) {
    int space_cnt = 0;

    //find white spaces
    for(int i = 0; i < length; i++) {
        if( input[i] == ' ') {
            space_cnt++;
        }
    }

    //replace with %20
    if( space_cnt != 0) {
        //work backwards so no afraid of overriding values when starting from the beginning
        int end = length + 2 * space_cnt; //for null char
        for(int i = length - 1; i >= 0 ; i--) {
            if(input[i] == ' ') {
                input[i + 2 * space_cnt] = '0';
                input[i + 2 * space_cnt - 1] = '2';
                input[i + 2 * space_cnt - 2] = '%';
                space_cnt--;
            }
            else {
                input[i + 2 * space_cnt] = input[i];
            }
        }

        input[end] = '\0';
    }
}