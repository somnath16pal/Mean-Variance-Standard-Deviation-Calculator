import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list to a 3x3 numpy array
    list = np.array(list).reshape((3, 3))

    # Prepare the calculations dictionary
    calculations = {}

    # Mean calculations
    calculations['mean'] = [list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), list.mean().tolist()]
    
    # Variance calculations
    calculations['variance'] = [list.var(axis=0).tolist(), list.var(axis=1).tolist(), list.var().tolist()]
    
    # Standard deviation calculations
    calculations['standard deviation'] = [list.std(axis=0).tolist(), list.std(axis=1).tolist(), list.std().tolist()]
    
    # Max calculations
    calculations['max'] = [list.max(axis=0).tolist(), list.max(axis=1).tolist(), list.max().tolist()]
    
    # Min calculations
    calculations['min'] = [list.min(axis=0).tolist(), list.min(axis=1).tolist(), list.min().tolist()]
    
    # Sum calculations
    calculations['sum'] = [list.sum(axis=0).tolist(), list.sum(axis=1).tolist(), list.sum().tolist()]

    return calculations

# Testing the function with the example input
print(calculate([9,1,5,3,3,3,2,9,0]))
