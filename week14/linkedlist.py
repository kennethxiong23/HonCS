"""
    Description: Creates a linked list object using the node class.
    Author: Kenneth
    Date: Fall 2021
"""
from node import *
class LinkedList(object):
    """class for list object"""
    def __init__(self):
        """ construct an empty linked list """
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item): 
        """ add new node, containing item, to end of the list """
        n = Node(item)
        if self.size == 0:
            self.head = n
            self.tail = n
            self.size = 1
        else:
            self.tail.setNext(n)
            self.tail = n
            self.size += 1

    def prepend(self, item):
        """add node, containing item, to the head of linked list"""
        n = Node(item)
        if self.size == 0:
            self.head = n
            self.tail = n
            self.size = 1
        else:
            n.setNext(self.head)
            self.head = n
            self.size += 1

    def __str__(self):
        """return string representation of linked list """
        s = "head-->"
        curr = self.head
        for i in range(self.size):
            s += ("(%s)"  %  str(curr.getItem()))
            curr = curr.getNext()
        s +=("<--tail")
        return s
        
    def __len__(self):
        """return how many nodes are in the linked list"""
        return self.size

    def __contains__(self, item):
        """returns true if an item is in the linked list"""
        node = self.head
        for index in range(self.size): #list traversal
            if node.getItem() == item:
                return True #return if item is in list
            node = self.head.getNext()
        return False
    
    def __getitem__(self, index):
        """returns the item at a given index"""
        if index < 0:
            index = self.size + index
        if index >= self.size:
            raise IndexError("index out of range")
        node = self.head
        for listIndex in range(self.size): #find the node at given index
            if listIndex == index:
                return node.getItem()
            node = node.getNext()
        return
           
    def __setitem__(self, index, item):
        """sets item at given index"""
        if index < 0: #convert negative index to positive
            index = self.size + index
        if index >= self.size:
            raise IndexError(" index out of range")
        else:
            if index == 0: #check for edge cases
                self.deleteHead()
                self.prepend(item)
            elif index == len(LL) - 1:
                self.deleteTail()
                self.append(item)
            else: #navigate through list to replace item in the middle
                node = Node(item)
                previousNode = self.head
                for listIndex in range(index - 1):
                    previousNode = previousNode.getNext()
                removeNode = previousNode.getNext()
                node.setNext(removeNode.getNext())
                previousNode.setNext(node)
                removeNode.setNext(None)

            return

    def deleteHead(self):
        """deletes node at head of linked list"""
        if self.size  == 0: #check edge cases
            return
        elif self.size == 1:
            oldHead = self.head
            self.head = None
            self.tail = None
            self.size = 0 
        else: #check middle of list
            oldHead = self.head
            newHead = oldHead.getNext()
            self.head = newHead
            self.size -= 1
        return oldHead.getItem()

    def deleteTail(self):
        """deletes node at tail of linked list"""
        if self.size == 0: #check edge cases
            return
        elif self.size == 1:
            oldTail = self.tail
            self.head = None
            self.tail = None
            self.size = 0 
        else:
            oldTail = self.tail
            newTail = self.head
            for i in range(self.size - 2): #navigates to the end of list
                newTail = newTail.getNext()
            self.tail = newTail
            self.size -= 1
        return oldTail.getItem()

    def count(self, item):
        """count and return the number of nodes that contain item"""
        amount = 0
        node = self.head
        for i in range(self.size): #find every time item occures
            if node.getItem() == item:
                amount += 1  
            node = node.getNext()
        return amount
    
    def index(self, item):
        """return the index of the first node that contains item"""
        node = self.head
        for index in range(self.size): #list traversal
            if node.getItem() == item:
                return index
            node = node.getNext()
        return -1

    def insert(self, index, item):
        """insert node containing item at given index"""
        if index <= 0: #check edge cases
            self.prepend(item)
        elif index >= self.size:
            self.append(item)
        else:
            node = Node(item)
            previousNode = self.head
            for id in range(1, index): #find node before the insert index
                previousNode = previousNode.getNext()
            node.setNext(previousNode.getNext()) #insert item into linked list
            previousNode.setNext(node)
            self.size += 1
        return
    
    def pop(self, index):
        """remove item at specified index and return the item"""
        if index < 0: #convert negaative index to positive
            index = self.size + index
        if self.size <= index:#check if index out of range
            return -1
        else:
            if index == 0: #check edge cases
                return self.deleteHead()
            elif index == self.size - 1:
                return self.deleteTail()     
            else:
                previousNode = self.head
                for id in range(0, index - 1): #go to the item before popped item
                    previousNode = previousNode.getNext()
                removeNode = previousNode.getNext() #remove item
                previousNode.setNext(removeNode.getNext())
                removeNode.setNext(None)
                self.size -= 1
                return removeNode.getItem()

    def remove(self, item):
        """remove first occurence of item in list"""
        if self.size == 0: #chcek if list is empty
            raise ValueError("item not in list")
        else: #check head
            if self.head.getItem() == item:
                self.deleteHead()
                return
            previousNode = self.head
            currentNode = previousNode.getNext()
            for index in range(self.size - 2): #lsit traversal
                if currentNode.getItem() == item: # check if item is in middle of list
                    break
                previousNode = previousNode.getNext()
                currentNode = currentNode.getNext()
            if currentNode.getItem() == item:
                previousNode.setNext(currentNode.getNext())
                currentNode.setNext(None)
                self.size -= 1
            elif item == self.tail.getItem(): #check the tail if not in middle
                self.deleteTail()
            else:
                raise ValueError("Item not in list") #error if not in list
            return 
           
if __name__ == "__main__":	# test the following methods: init, str, append, len
    #didn't test the delete methods or len, if they work code works
    LL = LinkedList()

    print("___tesing prepend, append___")
    assert len(LL) == 0			    
    assert str(LL) == "head--><--tail"
    LL.append("A")
    LL.prepend("B")
    LL.prepend("C")
    assert len(LL) == 3
    assert str(LL) == "head-->(C)(B)(A)<--tail" 

    #remove all items from list
    for i in range(len(LL)):
        LL.deleteHead()
    print("___testing insert___")
    LL.insert(0, "A")
    assert len(LL) == 1
    assert str(LL) == "head-->(A)<--tail" 
    LL.insert(len(LL) -1, "B")
    assert len(LL) == 2
    assert str(LL) == "head-->(B)(A)<--tail" 
    LL.insert(200,"D")
    assert len(LL) == 3
    assert str(LL) == "head-->(B)(A)(D)<--tail" 
    LL.insert(-200,"D")
    assert len(LL) == 4
    assert str(LL) == "head-->(D)(B)(A)(D)<--tail" 

    print("___testing remove___)")
    LL.remove("A")
    assert len(LL) == 3
    assert str(LL) == "head-->(D)(B)(D)<--tail" 
    LL.remove("D")
    assert len(LL) == 2
    assert str(LL) == "head-->(B)(D)<--tail" 
    LL.remove("D")
    assert len(LL) == 1
    assert str(LL) == "head-->(B)<--tail" 
    LL.remove("B")
    assert len(LL) == 0
    assert str(LL) == "head--><--tail" 
    
    print("___testing pop__")
    assert LL.pop(0) == -1
    assert str(LL) == "head--><--tail" 
    LL.append("A")
    LL.prepend("B")
    LL.prepend("C")
    assert LL.pop(3) == -1
    assert LL.pop(0) == "C"
    assert LL.pop(len(LL) - 1) == "A"
    assert str(LL) == "head-->(B)<--tail"

    print("___testing index___")
    assert LL.index("B") == 0
    assert LL.index("w") == -1
    LL.append("A")
    LL.prepend("B")
    LL.prepend("C")
    assert LL.index("B") == 1
    assert LL.index("A") == len(LL) - 1
    
    print("___Testing count___")
    assert LL.count("B") == 2
    assert LL.count("aweda") == 0
    assert LL.count("A") == 1

    print(LL)
    print("___testing Get item___")
    assert LL[-1] == "A"
    assert LL[0] == "C"
    
    print("___Testing set item___")
    LL[0] = "B"
    assert str(LL) == "head-->(B)(B)(B)(A)<--tail" 
    LL[-1] = "C"
    assert str(LL) == "head-->(B)(B)(B)(C)<--tail"
    print(LL)
    LL[-2] = "C"
    assert str(LL) == "head-->(B)(B)(C)(C)<--tail"  
    LL[2] = "D"
    print(LL)
    assert str(LL) == "head-->(B)(B)(D)(C)<--tail" 


    

   
    
    