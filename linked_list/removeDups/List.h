//
// Created by Rebecca Chow on 07/10/2018.
//
#ifndef REMOVEDUPS_LIST_H
#define REMOVEDUPS_LIST_H
struct Node {
    int data;
    Node* next;
};

class List{
public:
    List();
    virtual ~List();
    void appendNode(int data);
    bool removeNode(int data);

private:
    Node* head;
    Node* tail;
};
#endif //REMOVEDUPS_LIST_H
