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
            print("-----------------------------------------")
            print(f"Name: {tem.name} Age: {tem.age} Breed: {tem.breed} Date: {tem.date}")
            print("-----------------------------------------")
            tem = tem.next
    def dog_dequeue(self):
        tem = self.first
        if self.first==None:

            return False
        else:
            if self.first==self.last:
                self.first=None
                self.last=None
            else:
                self.first=tem.next
                tem.next=None

        self.length-=1
        return tem




my_queue=Queue()
selection=0
while True:
    print("\n")
    print("1.-Ingresar un Animalito")
    print("2.-Imprimir los animalitos disponibles")
    print("3.-Adoptar un Animalito")
    print("4.-Salir")
    selection=int(input())
    match selection:
        case 1:
            name=str(input("Ingresa el nombre del Animalito: \n"))
            age=int(input("Ingresa la edad del Animalito: \n"))
            breed=str(input("Ingresa la raza del Animalito: \n"))
            my_queue.dog_enqueue(name,age,breed)
        case 2:
            my_queue.print_queue()
        case 3:
            r = my_queue.dog_dequeue()
            if r==False:
                print("De momento ya no tenemos mas animalitos en adopcion")
            else:
                print("------------------------------------------")
                print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                print("------------------------------------------")
        case 4:
            print("Saliendo...")
            exit()