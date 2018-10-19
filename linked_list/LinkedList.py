import itertools

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dummy = Node(None)

    def __len__(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.nextNode
        return length

    def addNode(self, data):
        temp = self.head
        newNode = Node(data)
        if temp is None:
            self.head = newNode
            self.tail = self.head
            self.dummy.nextNode = self.head
        else:
            self.tail.nextNode = newNode
            self.tail = newNode


    def removeNode(self, data):
        prev = self.dummy
        cur = self.head
        while cur is not None:
            if cur.value == data:
                prev.nextNode = cur.nextNode
                if cur == self.head and cur == self.tail:
                    self.head = prev.nextNode
                    self.tail = self.head
                elif cur == self.head:
                    self.head = prev.nextNode
                elif cur == self.tail:
                    self.tail = prev
                return True
            cur = cur.nextNode

        return False


    def printNodes(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.nextNode
        print()


def createList():
    numbers = input("Enter a list of numbers: ")
    list_numbers = [int(i) for i in numbers.strip().split(" ")]
    newList = MyList()
    for i in list_numbers:
        newList.addNode(i)

    return newList


def printNodes(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.nextNode
    print()
