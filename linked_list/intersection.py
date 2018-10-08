from LinkedList import *

def intersection(head1, head2):
    #only work on special case link lists
    if head1 is None or head2 is None:
        return None

    runner1 = head1
    runner2 = head2

    while runner1 is not None or runner2 is not None:
        #works for the same length link list
        if runner1 is None and runner2 is not None:
            runner1 = head1
        elif runner1 is not None and runner2 is None:
            runner2 = head2
        if runner1 == runner2:
            return runner1
        runner1 = runner1.nextNode
        runner2 = runner2.nextNode

    return None

def generalIntersection(head1, head2):
    if head1 is None or head2 is None:
        return None

    length1, tail1 = getLengthandTail(head1)
    length2, tail2 = getLengthandTail(head2)

    if tail1 != tail2:
        return None
    else:
        diff = length1 - length2
        if diff > 0:
            longList = head1
            shortList = head2
        else:
            longList = head2
            shortList = head1

        for i in range(0, abs(diff)):
            longList = longList.nextNode

        while longList != shortList:
            longList = longList.nextNode
            shortList = shortList.nextNode


        return longList


def getLengthandTail(head):
    length = 1
    while head.nextNode is not None:
        length += 1
        head = head.nextNode
    tail = head
    return length, tail

def printNodesRefs(head):
    while head is not None:
        print(head, end=" ")
        head = head.nextNode
    print()

if __name__ == "__main__":
    list1 = createList() # 3 1 2
    list2 = createList() # 5 4 6
    #list2.tail.nextNode = list1.head
    #result = intersection(list2.head, list1.head)
    list2.tail.nextNode = list1.head.nextNode # list2 5 4 6 1 2
    printNodes(list2.head)
    result = generalIntersection(list1.head, list2.head)
    printNodesRefs(list1.head.nextNode)
    printNodesRefs(result)