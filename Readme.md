# This is a coding test for a Software Engineer Intern position at HOMEBASE.
**Note:** Before running any code, please make sure you have installed all the dependencies by running the following command: `pip install -r requirements.txt`
> All scripts written in Python have sample output files.
## Task 1: Python Programming
### Problem Statement
    Write a Python program that accomplishes the following:
    1. Reads a CSV file named "data.csv" containing two columns: "Name" and "Age".
    2. Calculates and prints the average age of individuals in the CSV file. 
    3. Gracefully handles potential errors or special cases.

### To run the code simply run the following command : `python task1/task1.py` 
> **Note:** You can put your own `data.csv` file in the task1 folder or the code will use `data_example.csv`.
## Task 2:  Data Structures: E-commerce Inventory Schema
### Problem Statement
    Design a data structure for an online store's inventory management system.
    1. Product Information: Store product details including Name, Description, Price, Quantity in stock, and Product type.
    2. Order Management: Define the structure to store order information, including Purchased Products, Order Date, Customer Information (Name, Address, Phone Number), and Order Status.
    3. Inventory Tracking: Design a structure to track inventory transactions, updating stock quantity after each transaction. Store transaction dates, quantity in/out, and associated products.
### Additional notes
    1. Describe relationships between tables or entities if applicable.
    2. Use appropriate data types (VARCHAR, INT, DATE, etc.) and apply constraints as needed.
> **Note:** I have used [dbdiagram.io] to design the database schema. You can find the schema in the `task2` folder or visit [https://dbdiagram.io/d/E-commerce-Inventory-Schema-659f98a5ac844320aeb09e87].

## Task 3:  Web Scraping - Real Estate Data from Batdongsan.com
### Problem Statement
    Write a Python script to extract real estate data from the website Batdongsan.com: 
    1. Scrape Real Estate Data: Scrape real estate listings from the Batdongsan.com website. Extract details such as property prices, availability, descriptions, and location.
    2. Caching Mechanism Implementation: Implement a caching mechanism to optimize scraping speed and prevent excessive requests to the server.
### To run the code simply run the following command : `python task3/task3.py` 

## Task 4: Nested Set Model Implementation
### Problem Statement
    Write a Python program to manipulate the Nested Set Model:
    1. Create Nested Set Model: Develop a function or class to convert hierarchical data into the nested set model.
    2. Retrieve Parent-Child Relationships: Calculate and organize parent-child relationships from the nested set model.
    3. Measure Performance: Optimize and evaluate the program's performance when dealing with nested sets on larger datasets.
### To run the code simply run the following command : `python task4/task4.py`

## Task 5: Database and SQL - Stored Procedure Creation
### Problem Statement
    Develop a stored procedure to manage blog posts in a relational database: 
    1. Stored Procedure Creation: Write a stored procedure in SQL to perform operations related to blog posts. Include functionalities for adding new posts, retrieving post details, updating posts, and deleting posts.
    2. Enhance Functionality: Implement additional functionalities within the stored procedure, such as managing user interactions like adding comments to posts, deleting comments, and fetching post-related data.
