'''

Class Implementation Practice

'''

class Queue:
    def __init__(self):
        self.Queue = [-1 for i in range(10)]
        self.HeadPointer, self.TailPointer = -1, -1

    def Enqueue(self, DataToEnq):
        if self.TailPointer >= 9:
            return False

        if self.TailPointer == -1 and self.HeadPointer == -1:
            self.HeadPointer, self.TailPointer = 0, 0
            self.Queue[self.TailPointer] = DataToEnq
            return True
        else:
            self.TailPointer += 1
            self.Queue[self.TailPointer] = DataToEnq
            return True

    def Dequeue(self):
        if self.TailPointer == -1 and self.HeadPointer == -1:
            return -1

        if self.TailPointer + 1 == self.HeadPointer:
            self.TailPointer, self.HeadPointer == -1, -1

        removed = self.Queue[self.HeadPointer]
        self.Queue[self.HeadPointer] = -1
        self.HeadPointer += 1
        return removed

queue = Queue()

for i in range(6):
    user_input = int(input("Enter a number: "))
    result = queue.Enqueue(user_input)
    if not result:
        print("Queue full")

print(f"Queue: {queue.Queue}\n")

for i in range(4):
    print(f"Removed: {queue.Dequeue()}")

print(f"Queue: {queue.Queue}\n")
