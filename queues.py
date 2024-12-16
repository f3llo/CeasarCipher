

class Queue:

    def __init__(self):
        self.que = []

    def enque(self, item):
        self.que.append(item)

    def deque(self):
        element = self.que[0]
        self.que = self.que[1:len(self.que)]
        return element

    def isEmpty(self):
        if len(self.que) == 0: return True
        else: return False

class PointerQueue:

    def __init__(self, n):
        self.que = [None]*n

