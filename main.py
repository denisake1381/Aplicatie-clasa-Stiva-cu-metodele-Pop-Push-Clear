# Tema L36 Python
# Folosind implementarea OOP a listelor inlantuite in Python implementati o clasa Stiva conform
# mecanismului LIFO care are 3 metode:
# a. Pop – elimina si returneaza varful stivei
# b. Push – adauga un element in varful stivei
# c. Clear – goleste stiva

class Nod:
    def __init__(self, val):
        self.val = val
        self.urmatorul = None

class Stiva:
    def __init__(self):
        self.varf = None
    
    def push(self, element):
        nod_nou = Nod(element)
        nod_nou.urmatorul = self.varf
        self.varf = nod_nou
    
    def pop(self):
        if self.varf is None:
            return None
        val = self.varf.val
        self.varf = self.varf.urmatorul
        return val
    
    def clear(self):
        self.varf = None

stiva = Stiva()
stiva.push(5)
stiva.push(10)
stiva.push(15)

print(stiva.pop())  
print(stiva.pop())  

stiva.push(20)
print(stiva.pop())  

stiva.clear()
print(stiva.pop())  
