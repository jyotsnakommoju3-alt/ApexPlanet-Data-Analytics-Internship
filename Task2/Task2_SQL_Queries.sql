-- Q1. Which products generate the highest total sales?
SELECT Product, SUM(Total_Sales) AS total_sales
FROM sales
GROUP BY Product
ORDER BY total_sales DESC;

-- Q2. Which product categories generate the most sales?
SELECT Category, SUM(Total_Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

-- Q3. Which cities generate the most sales?
SELECT City, SUM(Total_Sales) AS total_sales
FROM sales
GROUP BY City
ORDER BY total_sales DESC;

-- Q4. What is the monthly sales trend?
SELECT strftime('%Y-%m', Order_Date) AS month, SUM(Total_Sales) AS total_sales
FROM sales
GROUP BY strftime('%Y-%m', Order_Date)
ORDER BY month;

-- Q5. How do sales compare by gender?
SELECT Gender, COUNT(*) AS order_rows, SUM(Total_Sales) AS total_sales,
       AVG(Total_Sales) AS average_sales
FROM sales
GROUP BY Gender
ORDER BY total_sales DESC;

-- Q6. Which 10 customers have the highest total sales?
SELECT Customer_ID, SUM(Total_Sales) AS total_sales
FROM sales
GROUP BY Customer_ID
ORDER BY total_sales DESC
LIMIT 10;

-- Q7. How do order count and sales vary by customer age?
SELECT Age, COUNT(*) AS order_rows, SUM(Total_Sales) AS total_sales
FROM sales
GROUP BY Age
ORDER BY Age;
