#Q1
class myStack:
    def __init__(self):
        self.data=[]
        self.count=0
    def isEmpty(self):
        return self.count==0
    def getcount(self):
        return self.count
    def stackPush(self,x):
        self.data.append(x)
        self.count+=1
    def stackPop(self):
        if not self.isEmpty():
            self.count-=1
            return self.pop()
        else:
            return None
    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return None
    def displayInfo(self):
        print(self.data,self.count)

#Q2
def limited_stack(n):
	stack = []
	for i in range (1,n):
		stack.append(i)
	print(stack)


#Q3
class Stack:
      
    def __init__(self):
        self._arr = []
    def push(self, val):
        self._arr.append(val)
    def is_empty(self):
        return len(self._arr) == 0
    def pop(self):  
        if self.is_empty():
            print("Stack is empty")
            return          
        return self._arr.pop()
	def reverse_file(filename):
       
	    S = Stack()
	    original = open(filename)
	      
	    for line in original:
	        S.push(line.rstrip("\n"))	      
	    original.close()	       
	    output = open(filename, 'w')	      
	    while not S.is_empty():
	        output.write(S.pop()+"\n")
	      
	    output.close()
	filename = "reverse.txt"
	reverse_file(filename)
	with open(filename) as file:
	        for f in file.readlines():
	            print(f, end ="")
#Q4
open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"



#Q6
def Transfer(S, T):
 for i in range(len(S)):
   T.append(S.pop())
 return T
S = ["a","b","c","d"]
print(S)

T=[]
T = Transfer(S, T)
print(T)




