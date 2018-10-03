//
// Created by Rebecca Chow on 01/10/2018.
//

#ifndef ARRAY_STRING_MYHASHMAP_H
#define ARRAY_STRING_MYHASHMAP_H
#include <iostream>
#include "List.h"

class myHashMap {
public:

    myHashMap(int);
    virtual ~myHashMap();
    int hashKey(char);
    int getSize();
    List* arrayList;
private:
    int size;

};
#endif //ARRAY_STRING_MYHASHMAP_H
