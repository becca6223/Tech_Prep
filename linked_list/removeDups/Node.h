//
// Created by Rebecca Chow on 07/10/2018.
//

#ifndef REMOVEDUPS_NODE_H
#define REMOVEDUPS_NODE_H
class Node {
public:
    Node(int);
    virtual ~Node();
    int data;
    Node* next;
};

#endif //REMOVEDUPS_NODE_H
