class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self.prev = self

    def __str__(self):
        return str(self.key)


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __len__(self):
        return self.size

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return

        a.prev.next = b.next
        b.next.prev = a.prev
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)

    def pushBack(self, key):
        self.insertBefore(self.head, key)
        self.size += 1

    def delete(self, x):
        if x == None or x == self.head:
            return

        x.prev.next, x.next.prev = x.next, x.prev
        self.size -= 1
        return x.key

    def search(self, key):
        v = self.head.next
        while v != self.head:
            if v.key == key:
                return v
            v = v.next
        return None


N, K = map(int, input().split())
L = DoubleLinkedList()
ans = []

for i in range(1, N+1):
    L.pushBack(i)

v = L.head
while L:
    for i in range(1, K):
        if v.key == L.head.key:
            v = v.next
        x = L.search(v.key)
        L.pushBack(L.delete(x))
        v = v.next
    if v.key == L.head.key:
        v = v.next
    x = L.search(v.key)
    L.delete(x)
    ans.append(v.key)
    v = v.next

print("<", end="")
print(", ".join(str(v) for v in ans), end="")
print(">")
