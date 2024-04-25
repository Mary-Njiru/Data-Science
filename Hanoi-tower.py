# Using recursion
def tower_of_hanoi(num_disks, start, target, auxiliary):
    if num_disks == 1:
        print(f"Move disk 1 from {start} to {target}")
        return tower_of_hanoi(num_disks -1, start, auxiliary, target)
    print(f"Move disk {num_disks} from {start} to {target}")
    tower_of_hanoi(num_disks -1, auxiliary, target, start)

    num_disks = 6
    tower_of_hanoi(num_disks, "A", "C" "B")

# Using stacks data structure knowledge
class Stack:
  def __init__(self):
        self.items = []
def push(self, item):
            self.items.append(item)

def pop(self):
            if not self.is_empty():
                return self.items.pop()
            
def is_empty(self):
            return len(self.items) ==0
        
def peek(self):
            if not self.is_empty():
             return self.items[-1]
            
def towerOfHanoi(n):
            source = Stack()
            auxiliary = Stack()
            destination = Stack()

            for i in range(n, 0 , -1):
                source.push(i)

            if n%2 == 0 :
                temp = auxiliary
                auxiliary = destination
                destination = temp

            num_moves = 2**n -1

            for i in range(1, num_moves+1):
                if i % 3 ==1:
                    moveDisks(source,destination)
                
def __init__(self):
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem   A= [5,4,3,2,1]      B= []       C[] ")
        print()
        print("Expected Output A= []           B= []       C[5,4,3,2,1] ")
        self.A = []
        self.B = []
        self.C = []
def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")
def pass1(self):
        self.temp = self.A.pop(2)#A=[3,2,1]
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",  "B=",self.B   ,"   ","C=",self.C)
        print("Pass One Completed===============\n")
def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",  "B=",self.B   ,"   ","C=",self.C)
        print("Pass Two Completed===============\n")
def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)# B=[2,1]
        time.sleep(3)
        print("A=",self.A   ,"   ",  "B=",self.B   ,"   ","C=",self.C)
        print("Pass Three Completed=============\n")
def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",  "B=",self.B   ,"   ","C=",self.C)
        print("Pass Four Completed==============\n")
def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",  "B=",self.B   ,"   ","C=",self.C)
        print("Pass Five Completed==============\n")
def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",  "B=",self.B   ,"   ","C=",self.C)
        print("Pass Six Completed===============\n")
def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",  "B=",self.B   ,"   ","C=",self.C)
        print("Pass Seven Completed=============\n")
obj = tower('self','item')
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()