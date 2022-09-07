class Node:
    def __init__(self,name,ph,email):
        self.name = name
        self.phone = ph
        self.email = email
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.cnt = 0

    def createContact(self):
        name =  input("Enter the name = ")
        phone = input("Enter phone number = ")
        email = input("Enter the email  = ")
        temp = Node(name,phone,email)
        if self.head == None:
            self.head = temp
            #print(" -->", self.head.name)
        else:
            ptr = self.head
            while ptr.next!=None and temp.name > ptr.name :
                #print(temp.name , ptr.name)
                ptr=ptr.next
            if ptr==self.head and temp.name < ptr.name:
                temp.next = ptr
                ptr.prev=temp
                self.head = temp
            elif ptr.next==None and temp.name > ptr.name:
                ptr.next = temp
                temp.prev = ptr
            else:
                pp = ptr.prev
                pp.next = temp
                temp.prev = pp
                temp.next = ptr
                ptr.prev = temp
        self.cnt+=1

    def disp(self):
        if self.head == None:
            print("Contact list is empty")
        else:
            print("Contacts are = ")
            ptr = self.head
            while ptr!=None:
                print(f"{ptr.name}  {ptr.phone}   {ptr.email}")
                ptr=ptr.next


ob = DLL()
ob.createContact()
ob.disp()
ob.createContact()
ob.disp()
ob.createContact()
ob.disp()

