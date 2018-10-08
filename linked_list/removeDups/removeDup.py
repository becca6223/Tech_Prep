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



def removeDup(head):
    #first pass the list to check duplicates, store in hashmap
    nodeDict = {}
    temp = head

    while temp is not None:
        if temp.data in nodeDict:
            nodeDict[temp.data] += 1
        else:
            nodeDict[temp.data] = 1
        temp = temp.nextNode

    #pp(nodeDict)
    #second pass remove duplicates
    prev = head
    cur = head.nextNode
    while cur is not None:
        if nodeDict[cur.data] > 1:
            prev.nextNode = cur.nextNode
            nodeDict[cur.data] -= 1
        else:
            prev = cur

        cur = cur.nextNode

    #time complexity O(2n) -> O(n)

def removeDupSet(head):
    #One pass of the link list. Do scanning and removing at the same time
    nodeSet = set()
    prev = head
    cur = head.nextNode

    while cur is not None:
        if cur.data not in nodeSet:
            nodeSet.add(cur.data)
            prev = cur
        else:
            #it is in nodeSet. remove the node
            prev.nextNode = cur.nextNode

        cur = cur.nextNode




def createList():
    numbers = input("Enter a list of numbers: ")
    list_numbers = [int(i) for i in numbers.strip().split(" ")]
    newList = MyList()
    for i in list_numbers:
        newList.addNode(i)

    return newList


if __name__ == "__main__":
    newList = createList()
    newList.printNodes()
    removeDupSet(newList.head)
    newList.printNodes()


