
# 📋 Project Execution Plan

---

## 🚀 Phase 1: Understanding the Project and Data

### 🎯 Goal  
Understand what you are working on before writing any code.

### 📝 Tasks  
- 📌 Read the project description completely.  
- 📌 Understand that this is a Backend and Data Analysis project.  
- 📌 Identify the required types of analysis.  
- 📌 Understand the role of SQL vs MongoDB.

### ✅ Output  
- ✔ A clear mental picture of the whole project.
- ✅ Done 
---

## 🗂️ Phase 2: Understanding Tables and Relationships

### 🎯 Goal  
Understand the data structure and relationships.

### 📝 Tasks  

#### 📌 Identify Tables  
- Customers  
- Branches  
- Products  
- Sales  
- SaleDetails  

#### 🔑 Identify Keys  
- Primary Key for each table.  
- Foreign Key for each relationship.  

#### 🔗 Understand Relationships  
- Customer ➜ Sales  
- Sale ➜ SaleDetails  
- Branch ➜ Sales  
- Product ➜ SaleDetails  

### ✅ Output  
- ✔ Full understanding of data without writing code.
- ✅ Done 

---

## 📐 Phase 3: Drawing the ERD

### 🎯 Goal  
Convert understanding into a formal design.

### 📝 Tasks  
- 📌 Draw each table.  
- 📌 Add fields.  
- 📌 Show relationships.  
- 📌 Define relationship type: One-to-Many.  
- 📌 Save the diagram.

### ✅ Output  
- ✔ ERD ready for submission.
- ✅ Done 

---

## 📦 Phase 4: Drawing UML Class Diagram

### 🎯 Goal  
Represent the system as Classes.

### 📝 Tasks  
- 📌 Create a class for each entity:  
  - Customer  
  - Branch  
  - Product  
  - Sale  
  - SaleDetail  
  - DataWarehouseManager  
- 📌 Add attributes only.  
- 📌 Keep it simple.

### ✅ Output  
- ✔ Clear and simple UML diagram.

---

## 🛢️ Phase 5: Creating SQL Server Database

### 🎯 Goal  
Convert design into a real database.

### 📝 Tasks  
- 📌 CREATE DATABASE.  
- 📌 CREATE TABLE for each table.  
- 📌 Define Data Types.  
- 📌 Define Primary and Foreign Keys.  
- 📌 Run code and verify it works.

### ✅ Output  
- ✔ Clean and empty database.
- ✅ Done
---

## 🧪 Phase 6: Generating Fake Data

### 🎯 Goal  
Fill the database with realistic data.

### 📝 Tasks  
- 📌 Python script to generate data.  
- 📌 Insert:  
  - Customers  
  - Branches  
  - Products  
  - Sales  
  - SaleDetails  

### ⚠️ Considerations  
- Realistic dates.  
- Logical prices.  
- Correct relationships.

### ✅ Output  
- ✔ Database filled with data.
- ✅ Done
---

## 📊 Phase 7: Data Analysis Using SQL

### 🎯 Goal  
Ensure data is ready for analysis.

### 📝 Tasks  
- 📌 Basic SELECT queries.  
- 📌 JOIN tables.  
- 📌 GROUP BY.  
- 📌 Calculate:  
  - Total Sales  
  - Sales per Branch  
  - Sales per Customer  

### ✅ Output  
- ✔ Correct analytical queries.

---

## 📦 Phase 8: Moving Data to MongoDB

### 🎯 Goal  
Create a Data Warehouse.

### 📝 Tasks  
- 📌 Python script.  
- 📌 Extract aggregated data from SQL.  
- 📌 Structure as documents.  
- 📌 Insert into MongoDB.  

### 📄 Document Structure  
- Each document represents:  
  - One customer.  
  - Aggregated data.

### ✅ Output  
- ✔ MongoDB ready for analysis.

---

## 🌐 Phase 9: Building Flask API

### 🎯 Goal  
Create an interface to access data.

### 📝 Tasks  
- 📌 Create Flask app.  
- 📌 Endpoint for SQL data.  
- 📌 Endpoint for MongoDB data.  
- 📌 Return JSON.  
- 📌 Test endpoints.

### ✅ Output  
- ✔ Working API.

---

## 📈 Phase 10: Analysis and Visualization in Jupyter

### 🎯 Goal  
Extract value from data.

### 📝 Tasks  
- 📌 Call API.  
- 📌 Convert JSON to DataFrame.  
- 📌 Perform required analysis.  
- 📌 Draw charts:  
  - Bar  
  - Line  
  - Grouped  
  - Heatmap  
- 📌 Add clear titles.

### ✅ Output  
- ✔ Complete notebook.

---

## ✅ Phase 11: Review and Submission

### 🎯 Goal  
Ensure everything is completed.

### 📝 Tasks  
- 📌 ERD.  
- 📌 UML.  
- 📌 SQL Database.  
- 📌 MongoDB.  
- 📌 Flask API.  
- 📌 Jupyter Notebook.

### ✅ Output  
- ✔ Project ready for submission.

---

## 💡 Optional Improvements

- 📌 Add README file explaining:  
  - Project idea.  
  - Tools used.  
  - How to run the project.  

- 📌 Add Logging in Python and Flask.  
- 📌 Add Data Validation.  
- 📌 Add Basic Tests.  
- 📌 Organize folders:  
  - data_generation  
  - sql  
  - api  
  - analysis  
  - diagrams  
