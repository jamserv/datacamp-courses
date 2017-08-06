from Employee import Employee

def doIni():
    # Definition of savings and result
    savings = 100
    result = 100 * 1.10 ** 7

    # Fix the printout
    print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

    # Definition of pi_string
    pi_string = "3.1415926"

    # Convert pi_string into float: pi_float
    pi_float = float(pi_string)

    print (pi_float)

def recor():
    dias = {'Lun': 'Lunes', 'Mar': 'Martes'}
    meses = dict(ene= 'January', feb= 'Febrary')
    #iterate fisrt dictionary
    for index in dias:
        print dias[index]
        pass

    #iterate second dictionary
    for indej in meses:
        print meses[indej]
        pass

    #print key and value from dictionary
    for k,v in meses.items():
        print "%s -> %s" %(k,v)
        pass

emp1 = Employee("juan", 3800)
#print emp1.name + " gana %s " % emp1.salary
emp1.printNomin()

#recor()
#doIni()
