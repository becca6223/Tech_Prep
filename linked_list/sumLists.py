from LinkedList import *

def sumListsReverse(head1, head2):
    result1 = 0
    result2 = 0
    power_10 = 1

    #Get the sum of two lists
    while head1 is not None or head2 is not None:
        if head1 is not None:
            result1 += head1.data * power_10
            head1 = head1.nextNode
        if head2 is not None:
            result2 += head2.data * power_10
            head2 = head2.nextNode

        power_10 *= 10

    result = result1 + result2

    #store result back to reverse list
    dummy = Node(0)
    head = dummy
    while result != 0:
        remainder = result % 10
        result = int(result / 10)
        temp = Node(remainder)
        head.nextNode = temp
        head = temp

    return dummy.nextNode

def sumListsOrder(head1, head2):
    result1 = 0
    result2 = 0
    ten = 10

    # Get the sum of two lists
    while head1 is not None or head2 is not None:
        if head1 is not None:
            result1 = result1 * ten + head1.data
            head1 = head1.nextNode
        if head2 is not None:
            result2 = result2 * ten + head2.data
            head2 = head2.nextNode

    result = result1 + result2

    # store result back to order list
    tail = None
    while result != 0:
        remainder = result % 10
        result = int(result / 10)
        temp = Node(remainder)
        temp.nextNode = tail
        tail = temp

    return tail


if __name__ == "__main__":
    list1 = createList()
    list2 = createList()
    #head = sumListsReverse(list1.head, list2.head)
    head = sumListsOrder(list1.head, list2.head)
    printNodes(head)