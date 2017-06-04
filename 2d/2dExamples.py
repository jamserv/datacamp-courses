def _2darray():
    # Create baseball, a list of lists
    baseball = [[180, 78.4],
                [215, 102.7],
                [210, 98.5],
                [188, 75.2]]

    # Import numpy
    import numpy as np

    # Create a 2D numpy array from baseball: np_baseball
    np_baseball = np.array(baseball)

    # Print out the type of np_baseball
    print(type(np_baseball))

    # Print out the shape of np_baseball
    print(np_baseball.shape)

def _2dtest():
    import numpy as np
    # Create baseball, a list of lists
    baseball = [[180, 78.4],
                [215, 102.7],
                [210, 98.5],
                [188, 75.2]]
    np_baseball = np.array(baseball)
    print(np_baseball[3,:])
    print(np_baseball[3:])
    print(np_baseball[3,:1])

    #print(np_baseball[:,0])

def combineMatriz():
    import numpy as np
    age = [[1,2,3],
        [4,6,8]]
    xxx = np.array(age) * 2

def _2dArithmetic():
    baseball = [[180, 78.4],
                [215, 102.7],
                [210, 98.5],
                [188, 75.2]]

    updated = [[180, 78.4],
                [215, 102.7],
                [210, 98.5],
                [188, 75.2]]
    # baseball is available as a regular list of lists
    # updated is available as 2D numpy array

    # Import numpy package
    import numpy as np

    # Create np_baseball (3 cols)
    np_baseball = np.array(baseball)

    # Print out addition of np_baseball and updated
    print(np_baseball + updated)

    # Create numpy array: conversion
    conversion = np.array([0.0254, 0.453592, 1])

    # Print out product of np_baseball and conversion
    print(np_baseball * conversion)

_2dArithmetic()