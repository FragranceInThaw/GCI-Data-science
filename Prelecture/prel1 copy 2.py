import numpy as np

def homework(arr):
    a = np.asarray(arr)

    # Condition 1: multiple of 5
    is_multiple_of_5 = (a % 5 == 0)

    # Condition 2: nonzero remainder when divided by 2 (i.e., odd)
    is_odd = (a % 2 != 0)

    # Combine both conditions with logical AND
    mask = is_multiple_of_5 & is_odd
    return a[mask]


arr = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 3, 7])
result = homework(arr)
print(result)