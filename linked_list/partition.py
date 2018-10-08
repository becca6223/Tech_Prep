from LinkedList import MyList, createList, Node

def partition(head, value):
    dummy = Node(None)
    newHead = dummy
    tail = None
	
    while head is not None:
        temp = Node(head.data)
        if head.data < value:
            newHead.nextNode = temp
            newHead = temp
        else:
            temp.nextNode = tail
            tail = temp
        head = head.nextNode
        
    newHead.nextNode = tail
    
    return dummy.nextNode
    
def printNodes(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.nextNode
    print()
    
if __name__ == "__main__":
    newList = createList()
    value = input("value to be partition: ")
    head = partition(newList.head, int(value.strip()))
    printNodes(head)