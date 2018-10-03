//
// Created by Rebecca Chow on 01/10/2018.
//
#include <iostream>
#include <string>
#include "List.h"
#include "myHashMap.h"

int main(int argc, char* argv[]) {
    std::string input = "HiAreyoucl?";
    myHashMap hashMap = myHashMap(7);
    input[3] = 'a';

    for (std::string::iterator cur_char = input.begin(); cur_char != input.end(); cur_char++) {
        int key = hashMap.hashKey(*cur_char);
        int slot = key % hashMap.getSize();
        bool addChar = hashMap.arrayList[slot].addNode(*cur_char);
        if(!addChar) {
            std::cout << "This string doesn't have unique char" << std::endl;
            std::cout << "repeat char: ," << *cur_char << "," << std::endl;
            break;
        }
    }




    return 0;
}