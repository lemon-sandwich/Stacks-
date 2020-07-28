# --------------------------------------------------- #
# Reversing String

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class Stack:
    def __init__(self):
        self.top = None
    
    def reverse_string(self,data):
        for n in data:
            self.push(n)
        reversed = ""
        while not self.IsEmpty():
            reversed += self.pop()
        return reversed

    def push(self,data):
        if self.top is None:
            self.top = Node(data,None)
        else:
            n = Node(data,self.top)
            self.top = n
    
    def pop(self):
        if self.top is None:
            return " "
        n = self.top
        val = n.data
        self.top = self.top.next
        n.next = None
        del n
        return val

    def IsEmpty(self):
        return self.top == None
    
s = Stack()
print(s.reverse_string(input("String To Reverse: ")))

input("Press Any Other To Start The Braces Balancing Program\n")
# --------------------------------------------------------- #
# Balancing Braces

class Braces:
    def __init__(self):
        self.top = None
    
    def Equation(self,data):
        for n in data:
            if n == '(' or '{' or '[':
                self.push(n)
            elif n == ')':
                while result is not '(':
                    result = self.pop()
                    if result == '{' or '[' or None:
                        return False
                self.pop()
            elif n == '}':
                while result is not '{':
                    result = self.pop()
                    if result == '(' or '[' or None:
                        return False
                self.pop()
            elif n == ']':
                while result is not '[':
                    result = self.pop()
                    if result == '{' or '(' or None:
                        return False
                self.pop()
        return True

    def push(self,data):
        if self.top is None:
            self.top = Node(data,None)
        else:
            n = Node(data,self.top)
            self.top = n
    
    def pop(self):
        if self.top is None:
            return None
        n = self.top
        val = n.data
        self.top = self.top.next
        n.next = None
        del n
        return val

    def IsEmpty(self):
        return self.top == None

b = Braces()

if b.Equation(input("Equation With Braces To Check Braces Validity: ")):
    print("Valid")
