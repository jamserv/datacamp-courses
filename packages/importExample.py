def importMethod():
    # Definition of radius
    r = 0.43

    # Import the math package
    import math

    # Calculate C
    C = 2 * math.pi * r

    # Calculate A
    A = math.pi * r ** 2

    # Build printout
    print("Circumference: " + str(C))
    print("Area: " + str(A))

def radiansImport():
    # Definition of radius
    r = 192500

    # Import radians function of math package
    from math import radians

    # Travel distance of Moon over 12 degrees. Store in dist.
    dist = r * radians(12)

    # Print out dist
    print(dist)

def np_array():
    # Create list baseball
    baseball = [180, 215, 210, 210, 188, 176, 209, 200]

    # Import the numpy package as np
    import numpy as np

    # Create a numpy array from baseball: np_baseball
    np_baseball = np.array(baseball)

    # Print out type of np_baseball
    print(type(np_baseball))

def baseball_players_height():
    # height is available as a regular list
    height = [1,2,3]

    # Import numpy
    import numpy as np

    # Create a numpy array from height: np_height
    np_height = np.array(height)

    # Print out np_height
    print(np_height)

    # Convert np_height to m: np_height_m
    np_height_m = np_height * 0.0254

    # Print np_height_m
    print(np_height_m)

def multiplicacion():
    # height and weight are available as a regular lists
    height = [1, 2, 3]
    weight = [1, 2, 3]

    # Import numpy
    import numpy as np

    # Create array from height with correct units: np_height_m
    np_height_m = np.array(height) * 0.0254

    # Create array from weight with correct units: np_weight_kg
    np_weight_kg = np.array(weight) * 0.453592

    # Calculate the BMI: bmi
    bmi = np.array(np_weight_kg / np_height_m ** 2)

    # Print out bmi
    print(bmi)

def minorArray():
    # Import numpy
    import numpy as np
    height = [1, 2, 3]
    weight = [1, 2, 3]

    # Calculate the BMI: bmi
    np_height_m = np.array(height) * 0.0254
    np_weight_kg = np.array(weight) * 0.453592
    bmi = np_weight_kg / np_height_m ** 2

    # Create the light array
    light = np.array(bmi < 21)

    # Print out light
    print(light)

    # Print out BMIs of all baseball players whose BMI is below 21
    print(np.array(bmi[light]))

minorArray()