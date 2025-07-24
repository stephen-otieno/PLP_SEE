# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    #Add to front 
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    # print list
    def print_list(self):
        current = self.head
        
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(10) 
    ll.insert_front(20)
    ll.insert_front(30)
    ll.insert_front(40)
    
    ll.print_list()
    
    
#LIFO Last in First Out

# Doubly LinkedList

class DNone:
    def __init__(self,data):
        self.data = data # Value stored in the node
        self.prev = None # Pointer to the previous node
        self.next = None # Pointer to the next node
        
        
# Node holds:
# - Data = value (e.g 10,apples,x)
# - Next = pointer that points to the next Node in the list


# Example

# [10 | next]--> [20 | next] --> [30 | next] --> None

class LinkedList:
    def __init__(self):
        self.head = None # Start of the list