from LinkedList import *

def isPalindrome(list1):
    length = len(list1)

    if length <= 1:
       return True

    #Traverse the link list half way
    temp = list1.head
    stack = []
    for i in range(0, int(length / 2)):
        stack.append(temp.data)
        temp = temp.nextNode

    #temp right now is at the middle of the list
    if length % 2 == 1:
        #the linked list is odd
        temp = temp.nextNode

    while temp is not None:
        if temp.data != stack.pop():
            return False
        temp = temp.nextNode

    return True

def isPalindromeNumber(number):
    pass

if __name__ == "__main__":
    newList = createList()
    result = isPalindrome(newList)
    print(result)

