class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        return ("{}".format(self.value)) 

    __repr__ = __str__
                          
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def insert(self, after, item):
        #adds a new Node with value= item to the list after the Node with value=after. Returns nothing.
        new_node= Node(item)
        temp= self.head
        while temp.value != after:
            temp= temp.next
        new_node.next= temp.next
        temp.next= new_node
        self.count+=1

    def pop(self):
        #removes and returns the value of the last Node in the list. It needs no parameter and modifies the list and returns an item.
        val= self.tail.value
        temp= self.head

        while temp.next!= self.tail:
            temp= temp.next
        self.tail= temp
        temp.setNext(None)
        
        self.count-=1
        return val
    

    def append(self, value):
        #adds a new Node with value= item to the end of the list. It returns nothing.
        if self.head==None:
            new_node=Node(value)
            self.head=new_node
            self.tail=self.head
        elif self.tail==self.head:
            self.tail=Node(value)
            self.head.setNext(self.tail)
        else:
            new_node=Node(value)
            self.tail.setNext(new_node)
            self.tail=new_node
        self.count+=1


    def remove(self, value):
        #removes the Node with value= item in the list.
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getValue()==value:
                found=True
            else:
                previous=current
                current=current.getNext()

        if previous==None:
            self.head=current.getNext()
        elif current.getNext()==None:
            self.tail=previous
            previous.setNext(None)
        else:
            previous.setNext(current.getNext()) 

        self.count-=1


    def isEmpty(self):
        #tests to see whether the list is empty. Returns a boolean value.
        return self.head == None

    def size(self):
        #returns the number of items in the list. Returns an integer.
        return self.count

    def add(self, value):
        #adds a new Node with value= item to the beginning of the list.
        new_node=Node(value)
        new_node.setNext(self.head)
        self.head=new_node
        self.count+=1

        if self.size()==1:
            self.tail=new_node


    def search(self,value):
        #searches for the Node with value= item in the list. Returns a boolean value.
        current=self.head
        found=False
        while current!=None and not found:
            if current.getValue()==value:
                return True
            else:
                current=current.getNext()
        return found


    def printList(self):
        temp=self.head
        while temp:
            print(temp.value, end=' ')
            temp=temp.next
