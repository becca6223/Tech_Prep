from LinkedList import *

def loopDetect(head):
    #From cracking the code interview
    slow = head
    fast = head

    while head is not None and head.nextNode is not None:
        slow = slow.nextNode
        fast = fast.nextNode.nextNode
        if slow == fast:
            break

    if fast is None or fast.nextNode is None:
        return None

    slow = head

    while fast != slow:
        fast = fast.nextNode
        slow = slow.nextNode

    return fast


if __name__ == "__main__":
    list1 = createList()
    list1.tail.nextNode = list1.head.nextNode.nextNode.nextNode
    result = loopDetect(list1.head)
    print(result.data)
