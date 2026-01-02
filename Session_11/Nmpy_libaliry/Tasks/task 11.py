import numpy as np

#%% Task: Sales Data Analysis (Advanced)
"""
# 🔹 Scenario:
You have sales data for 4 stores over 7 days (1 week).  
- The data is a 4x7 array (rows = stores, columns = days).  

Task:
1. Create a random integer array of shape 4x7 representing daily sales (values 50-200).  
2. Calculate total weekly sales for each store.  
3. Calculate average sales per day across all stores.  
4. Find the store with the highest total weekly sales.  
5. Normalize the sales data (0-1) for ML preprocessing.  
6. Extract sales of stores 2 and 3 for days 3-5.  
7. Simulate a 10% sales increase for all stores on the weekend (columns 5 & 6).  
8. Reshape the data into a single column vector for storage.  
"""

# 1️⃣ Create random sales data
sales_data = np.random.randint(50, 201, (4,7))
print("Original Sales Data (4x7):\n", sales_data)

# 2️⃣ Total weekly sales per store
weekly_sales = sales_data.sum(axis=1)
print("\nTotal Weekly Sales per Store:", weekly_sales)

# 3️⃣ Average sales per day across all stores
avg_daily_sales = sales_data.mean(axis=0)
print("\nAverage Daily Sales:", avg_daily_sales)

# 4️⃣ Store with highest total weekly sales
best_store = np.argmax(weekly_sales)
print("\nStore with Highest Weekly Sales (index):", best_store)

# 5️⃣ Normalize sales data (0-1)
normalized_sales = (sales_data - sales_data.min()) / (sales_data.max() - sales_data.min())
print("\nNormalized Sales Data:\n", normalized_sales)

# 6️⃣ Extract sales of stores 2 and 3 for days 3-5
subset_sales = sales_data[1:3, 2:5]
print("\nSales of stores 2 & 3 for days 3-5:\n", subset_sales)

# 7️⃣ Simulate 10% sales increase for weekend (columns 5 & 6)
sales_data[:, 5:7] = (sales_data[:, 5:7] * 1.1).astype(int)
print("\nSales Data after 10% Weekend Increase:\n", sales_data)

# 8️⃣ Reshape into single column vector
sales_vector = sales_data.reshape(-1,1)
print("\nSales Data as Single Column Vector:\n", sales_vector)