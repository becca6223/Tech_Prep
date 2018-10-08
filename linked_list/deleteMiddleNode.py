from LinkedList import MyList, createList

def deleteMiddleNode(node):
    pt1 = node
    pt2 = node.nextNode 
    
    while pt2 is not None: 
        pt1.data = pt2.data
        prev = pt1
        pt1 = pt1.nextNode
        pt2 = pt2.nextNode
    
    prev.nextNode = None
        
def getNode(head, k):
    #assume kth Node is neither head nor tail
    temp = head
    for i in range(0,k):
        temp = temp.nextNode
        
    return temp
    

if __name__ == "__main__":
    newList = createList()
    number = input("Kth Node, k is: ")
    randNode = getNode(newList.head, int(number.strip()))
    deleteMiddleNode(randNode)
    newList.printNodes()
    
    
    
