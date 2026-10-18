StartLinkedList = 2
StartEmptyList = 7
LinkedList = [[9512, 5], 
              [5541, 3], 
              [1999, 0], 
              [6651, -1], 
              [-1, 6], 
              [5612, 1], 
              [-1, -1],
              [-1, 4]]

def PrintListItems():
    global StartEmptyList, StartLinkedList, LinkedList
    if StartLinkedList == -1:
        print("Linked list is empty")
    else:
        curr = LinkedList[StartLinkedList]
        while curr[1] != -1:
            print(curr[0])
            curr = LinkedList[curr[1]]
        print(curr[0])

def PrintEmptyList():
    global StartEmptyList, StartLinkedList, LinkedList
    if StartEmptyList == -1:
        print("Empty list is empty")
    else:
        curr = LinkedList[StartEmptyList]
        while curr[1] != -1:
            print(curr[0])
            curr = LinkedList[curr[1]]
        print(curr[0])

print('Linked List:')
PrintListItems()
print('Empty List:')
PrintEmptyList()

def AddItem(DataToInsert):
    global StartEmptyList, StartLinkedList, LinkedList
    total = 0
    if StartEmptyList == -1: 
        print("List is full")
    elif LinkedList[StartLinkedList][0] == -1:
        LinkedList[StartLinkedList][0] = DataToInsert
        LinkedList[StartLinkedList][1] = -1
    else:
        LinkedList[StartEmptyList][0] = DataToInsert
        curr = LinkedList[StartLinkedList]
        while curr[1] != -1:
            total += 1
            curr = LinkedList[curr[1]]

        curr[1] = StartEmptyList
        StartEmptyList = LinkedList[curr[1]][1]
        curr = LinkedList[curr[1]]
        total += 1
        curr[1] = -1

        # print(f'{DataToInsert} was successfully inserted into linked list')
        
        if total == 8:
            StartEmptyList = -1

print()
AddItem(2345)
AddItem(2345)
AddItem(2345)
AddItem(2345)
AddItem(2345)

print('New Linked List:')
PrintListItems()
print('New Empty List:')
PrintEmptyList()
