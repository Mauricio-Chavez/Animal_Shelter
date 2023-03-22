import datetime
class Dog:
    def __init__(self,name,age,breed,date):
        self.name=name
        self.age=age
        self.breed=breed
        self.date=date
        self.next=None

class Queue:
    def __init__(self):
        self.first=None
        self.length=0
        self.last=None
    def dog_enqueue(self,name,age,breed):
        date=datetime.datetime.now()
        new_node=Dog(name,age,breed,date)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return
    def print_queue(self):
        tem=self.first
        while tem is not None:
            print(tem.name)
            print(tem.age)
            print(tem.breed)
            print(tem.date)
            print("---------------------------")
            tem = tem.next
    def dog_dequeue(self):
        tem = self.first
        if self.first==self.last:
            self.first=None
            self.last=None
        else:
            self.first=tem.next
            tem.next=None

        self.length-=1
        return tem
my_queue=Queue()
my_queue.dog_enqueue("Fred",3,"Chihuaha")
my_queue.dog_enqueue("Fred2",3,"Pastor Aleman")
my_queue.print_queue()
r=my_queue.dog_dequeue()
print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
print("------------------------------------------")
my_queue.print_queue()