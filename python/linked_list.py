from urllib.parse import _NetlocResultMixinBytes


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self,data):
        node = Node(data, self.head)
        print(node)
        self.head = node
        

ll = LinkedList()
ll.insert_at_beg(5)
ll.insert_at_beg(55)
