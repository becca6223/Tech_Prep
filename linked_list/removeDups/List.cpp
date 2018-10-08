//
// Created by Rebecca Chow on 07/10/2018.
//

#include "List.h"

List::List():head(nullptr), tail(nullptr){}
List::~List(){}

void List::appendNode(int value) {
    Node* temp = new Node;
    temp -> data = value;
    temp -> next = nullptr;
    if (head == nullptr) {
        head = temp;
        tail = temp;
    }
    else {
        tail -> next = temp;
        tail = temp;
    }
}

bool List::removeNode(int value) {
    Node* temp = head;
    while (temp != nullptr) {

    }
}