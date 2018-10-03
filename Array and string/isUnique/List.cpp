//
// Created by Rebecca Chow on 01/10/2018.
//

#include "List.h"

List::List():head(nullptr),tail(nullptr) {}

List::~List() {}

bool List::addNode(char value) {
    if(!findNode(value)) {
        Node *temp = new Node;
        temp->data = value;
        temp->next = nullptr;
        if(tail == nullptr) {
            tail = temp;
            head = temp;
        }
        else {
            tail->next = temp;
            tail = temp;
        }
        return true;
    }
    return false;
}

bool List::findNode(char value) {
    Node* temp = head;
    while (temp != nullptr) {
        if(temp -> data == value ) {
            return true;
        }
        temp = temp -> next;
    }

    return false;
}