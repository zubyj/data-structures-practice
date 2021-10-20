class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    # Traverse through n elements : O(n)
    def insertAtTail(self, node):
        # if head is empty, add to head
        if (self.head == None):
            self.head = node
            return
        # else add to tail 
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        curr.next = node

    # Only looking at head node : O(1)
    def insertAtHead(self, node):
        node.next = self.head
        self.head = node

    # A -> B -> C -> D
    #         B
    # insert another B at index 2 (pos 3)
    # A -> B -> B -> C -> D

    # move pointer to index - 1
    # set the nodes next to equal next.next
    # Worst case, traversing through all elems
    #   if index at end of list : O(n)
    def insert(self, index, node):
        # check if valid index
        if index < 0:
            print('enter valid index')
            return

        curr = self.head
        pos = 0
        while (pos != index-1):
            curr = curr.next
            pos += 1
        node.next = curr.next
        curr.next = node

    # A -> B -> C -> D
    # remove at index 2
    # 1. iterate to index - 1
    # 2. set node.next = node.next.next
    def remove(self, index):
        # removing head
        if (index == 0):
            self.head = self.head.next
            return

        curr = self.head
        pos = 0
        while (pos != index-1):
            curr = curr.next
            pos += 1
        curr.next = curr.next.next
    
    def showList(self):
        out = 'head -> '
        curr = self.head
        while (curr != None):
            out += (curr.data + ' -> ')
            curr = curr.next
        return out

def main():
    ll = LinkedList()
    n1 = Node('zuby')
    n2 = Node('javed')
    ll.insertAtTail(n1)
    ll.insertAtTail(n2)
    n3 = Node('bin-munir')
    ll.insert(1, n3)
    ll.remove(1)
    print(ll.showList())

if __name__ == "__main__":
    main()
