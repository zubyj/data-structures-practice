class Node:
    def __init__(self, data=None, next = None, prev = None):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printlist(self):
        print("Printing List")
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def insertAtHead(self, node):
        node.next = self.head
        node.prev = None
        self.head = node

    def insertAtTail(self, node):
        # empty list
        if self.head == None:
            self.head = node
            return

        # tail is null  
        if self.tail == None:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            node.prev = curr
            self.tail = node
            return
        
        # general case
        oldTail = self.tail
        oldTail.next = node
        node.prev = oldTail
        self.tail = node

    
    def insertAfterNode(self, node, newNode):
        return


list = DLinkedList()
# list.insertAtHead(Node("Lebron"))
# list.insertAtHead(Node("Durant"))
# list.insertAtTail(Node("Curry"))
# list.insertAtHead(Node("Jordan"))
list.insertAtTail(Node("Johnson"))
list.printlist()





