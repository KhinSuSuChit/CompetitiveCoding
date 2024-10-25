class PQueue:
    def __init__(self):
        self.array = []

    def isEmpty(self):
        return len(self.array) == 0

    def enqueue(self, data, priority):
        index = 0
        while index < len(self.array) and self.array[index][1] <= priority:
            index += 1
        self.array.insert(index, (data, priority))

    def deQueue(self):
        if self.isEmpty():
            print("Queue underflow")
        else:
            return self.array.pop(0)[0]

    def size(self):
        return len(self.array)

pq = PQueue()
pq.enqueue(10, 5)
pq.enqueue(12, 2)
pq.enqueue(13, 1)
pq.enqueue(7, 3)
pq.enqueue(54, 4)

l = []
while not pq.isEmpty():
    m = pq.deQueue()
    l.append(m)

p = 1
for i in range(len(l)-1, max(len(l)-4, -1), -1):
    p *= l[i]

print("Product of three largest elements is:", p)
