from pprint import pprint as pp

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dummy = Node(None)

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

def kth_to_lastElement_wrapper(head,k):
    #This function return all the elements from kth to last to the last element
    if head is not None:
        result = kth_to_lastElement(head, 0, k)

        return result

def kth_to_lastElement(head, n, k):
    if head is not None:
        result, length = kth_to_lastElement(head.nextNode, n+1, k)
        if length - k >= 0:
            result.insert(0, head.data)
            length -= 1
        return result, length
    else:
        return [], n

def iter_kth_to_lastElement(head, k):
    pt1 = head
    pt2 = head
    for i in range(0, k):
        if pt2 is None:
            return None
        else:
            pt2 = pt2.nextNode

    while pt2 is not None:
        pt1 = pt1.nextNode
        pt2 = pt2.nextNode

    return pt1

def createList():
    numbers = input("Enter a list of numbers: ")
    list_numbers = [int(i) for i in numbers.strip().split(" ")]
    newList = MyList()
    for i in list_numbers:
        newList.addNode(i)

    return newList


if __name__ == "__main__":
    newList = createList()
    #newList.printNodes()
    number = input("kth element: ")
    #result, a = kth_to_lastElement_wrapper(newList.head, int(number.strip()))
    #newList.printNodes()
    kth_node = iter_kth_to_lastElement(newList.head, int(number.strip()))
    print(kth_node, kth_node.data)


