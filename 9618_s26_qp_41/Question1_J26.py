Queue = [-1 for i in range(10)] #QUEUE 10 SPACES INTEGER
HeadPointer = -1 #INTEGER
TailPointer = -1 #INTEGER

def Enqueue(DataToEnq):
    global TailPointer, HeadPointer, Queue
    if TailPointer >= 9:
        return False

    if TailPointer == -1 and HeadPointer == -1:
        HeadPointer, TailPointer = 0, 0
        Queue[TailPointer] = DataToEnq
        return True
    else:
        TailPointer += 1
        Queue[TailPointer] = DataToEnq
        return True

for i in range(6):
    user_input = int(input("Enter a number: "))
    result = Enqueue(user_input)
    if not result:
        print("Queue full")



def Dequeue():
    global TailPointer, HeadPointer, Queue
    if TailPointer == -1 and HeadPointer == -1:
        return -1

    if TailPointer + 1 == HeadPointer:
        TailPointer, HeadPointer == -1, -1

    removed = Queue[HeadPointer]
    HeadPointer += 1
    return removed

for i in range(4):
    print(f"Removed: {Dequeue()}")

print(f"Queue: {Queue}\n")
