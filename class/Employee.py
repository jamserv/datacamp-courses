class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printNomin(self):        
        print (self.name + " gana %s " % self.salary)
