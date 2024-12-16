
class ListNode: #singly linked list
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = None

    def prepend(self, item):
        newNode = ListNode(item)
        newNode.next = self.head
        self.head = newNode

    def traverse(self):
        curNode = head
        while curNode != None:
            print(curNode.data)
            curNode = curNode.next
    
    def unordered_search(self, target):
        curNode = self.head
        while curNode != None && curNode != target:
            curNode = curNode.next
        return curNode is not None

    def remove(self, target):
        prevNode = None
        curNode = self.head
        while curNode != None && curNode != target:
            prevNode = curNode
            curNode.next
        if curNode.next != None:
            if curNode == self.head:
                self.head = curNode.next
            else:
                prevNode.next = curNode.next
        
    def add(self, target, node):
        prevNode = None
        curNode = self.head
        while curNode != None && curNode != target:
            curNode = prevNode
            curNode.next
        if curNode.next != None && prevNode != None:
            prevNode.next = node
            node.next = curNode.next








