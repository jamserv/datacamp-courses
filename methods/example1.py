def capitalizeExample():
    str = 'juan carlos anez mejias'            
    str1 = str.capitalize()
    print str1

def replaceExample():
    str = 'juan carlos'
    str1 = str.replace('a','u')
    
    print str1


#caiman append example
def appendExample():
    fam = ['karelys','roi']
    fam.append("me")
    
    print fam
    
def upperExample():
    # string to experiment with: room
    room = "poolhouse"

    # Use upper() on room: room_up
    room_up = room.upper()

    # Print out room and room_up
    print(room)
    print(room_up)

    # Print out the number of o's in room
    print(room.count("o"))    
    
def listMetho():
    # Create list areas
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Print out the index of the element 20.0
    print(areas.index('11.25'))

    # Print out how often 14.5 appears in areas
        
    
listMetho()