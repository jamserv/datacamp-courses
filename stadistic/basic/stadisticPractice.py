
def example1stadistic():
    import numpy as np

    height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
    weight = np.round(np.random.normal(60.32, 15, 5000), 2)

    np_city = np.column_stack((weight, height))

    print(np_city)

def averagexample():
    import numpy as np
    x = [1,4,8,10,12, 16]

    #mean = media
    print(np.mean(x))

    print(np.median(x))

def t1cua():
    import numpy as np
    ok = [[1,2,3], [4,5,6]]

    v1 = np.array(ok)
    print(v1[:,2])
    print('std :: %s' %np.std(v1[:,0]))
    print('median :: %s' % np.mean(ok))
    print('correlation :: %s' % np.corrcoef(v1[:,0], v1[:,1]))

t1cua()