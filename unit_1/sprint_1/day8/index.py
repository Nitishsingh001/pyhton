# 📌 Day 8: Working with Libraries (NumPy, Pandas)
# Topics:

# NumPy arrays (np.array, reshape, slicing)

# Pandas (DataFrame, Series, read_csv, groupby)

# Basic data analysis (mean, sum, filtering)


import numpy as np
import pandas as pd
# arr  = np.array([1,2,3,4,5])
# print()


# import numpy as np

# arr = np.array([1, 2, 3, 4])
# print(arr)
# print(type(arr))



# np.zeros((2, 3))     # 2x3 array of 0s
# np.ones((2, 3))      # 2x3 array of 1s
# np.eye(3)            # 3x3 identity matrix
# np.full((2, 2), 7)   # 2x2 array filled with 7




# a = np.array([[1, 2, 3], [4, 5, 6]])

# print(np.sum(a))       # 21
# print(np.mean(a))      # 3.5
# print(np.min(a))       # 1
# print(np.max(a))       # 6

# # Axis-wise operation
# print(np.sum(a, axis=0))  # [5 7 9] → column-wise
# print(np.sum(a, axis=1))  # [6 15] → row-wise


# arr = np.array([1, 2, 3, 4, 5])

# print(np.mean(arr))     # Average
# print(np.median(arr))   # Median
# print(np.std(arr))      # Standard deviation
# print(np.sum(arr))      # Total sum
# print(np.max(arr))      # Maximum
# print(np.min(arr))      # Minimum



data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)




data = {
    "Name": ["nitish", "golu","last"],
    "age": [20, 21, 22],
    "city": ["delhi", "mumbai", "pune"]
}

df = pd.DataFrame(data)
print(df)

# goruping data 


data = {
    "Department": ["HR", "IT", "HR", "Finance", "IT"],
    "Salary": [40000, 50000, 45000, 60000, 52000]
}

df = pd.DataFrame(data)

# Group by Department and get average salary
print(df.groupby("Department")["Salary"].mean())


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
print(df)
