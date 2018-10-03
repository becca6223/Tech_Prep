//
// Created by Rebecca Chow on 01/10/2018.
//

#ifndef ARRAY_AND_STRING_LIST_H
#define ARRAY_AND_STRING_LIST_H
struct Node {
    int data;
    Node* next;
};

class List{
public:
    List();
    virtual  ~List();
    bool addNode(char);
    bool findNode(char);
private:
    Node* head;
    Node* tail;
};
#endif //ARRAY_AND_STRING_LIST_H
