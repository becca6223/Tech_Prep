//
// Created by Rebecca Chow on 02/10/2018.
//
#include "myHashMap.h"

myHashMap::myHashMap(int user_size){
    size = user_size;
    arrayList = new List[size];
}

myHashMap::~myHashMap() {}

int myHashMap::hashKey(char value) {
    return value;
}

int myHashMap::getSize() {
    return size;
}



