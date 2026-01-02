import numpy as np

#%% Task 7
# 🔹 From the array [[1,2,3],[4,5,6],[7,8,9]], extract the elements 2, 5, 8 using slicing
arr_task7 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_task7_result = arr_task7[:,1]
print("Task 7:", arr_task7_result)
