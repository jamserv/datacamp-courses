def simpleList():
    days = {"lun": 'lunes', 'mar': 'martes', 1:2, 2:False, 3: 18772768, 'pi:': 3.141564}
    #print only values
    for index in days:
        print(days[index])

    #print key and value
    for k,v in days.items():
        print (k,v)

def practice_list_1():
    hall = 11.25
    kit = 18.0
    liv = 20.0
    bed = 10.75
    bath = 9.50
    """    
    Create a list, areas, that contains the area of the: 
    hallway (hall), 
    kitchen (kit), 
    living room (liv), 
    bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
    Print areas with the print() function.
    """
    areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed , "bathroom", bath]    
                
    print(areas)
    
    print(type(areas))
    
def practice_sublist_2():
    # Create the areas list
    areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]        
    # Print out second element from areas
    print(areas[1])
    # Print out last element from areas
    print(areas[9])
    # Print out the area of the living room
    print(areas[5])
    
    # the sum of the area of the kitchen and the area of the bedroom
    eat_sleep_area =  areas[3] + areas[7]
    
    print(eat_sleep_area)
    
def Slicing_and_dicing():
    areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]        
    
    #downstairs = areas[0:6]    
    #upstairs = areas[6:10]

    downstairs = areas[:6]
    upstairs = areas[6:]
    
    print(downstairs)
    print(upstairs)
    
def createOtherList():
    areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
    areas_1 = areas + ["garage", 15.65]        
    
    print(areas_1)

def listIndex():
    # Create list areas
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Print out the index of the element 20.0
    print(areas.index(20.0))

    # Print out how often 14.5 appears in areas
    print(areas.count(14.5))
    
listIndex()