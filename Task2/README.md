# ApexPlanet Data Analytics Internship — Task 2

## Contents
- `Task2_EDA_Analysis.xlsx`: analysis workbook with cleaned data, summary metrics, product/category/city/monthly summaries, SQL-result sheets, and a dashboard mock-up.
- `Task2_SQL_Queries.sql`: seven SQLite-compatible business questions.
- `Task2_EDA_Report.docx`: EDA report with charts, summary statistics, findings, and limitations.

## Dataset preparation
Source workbook: 1,000 rows, 12 original columns.
- Parsed `Order_Date` as a date.
- Filled missing `Age` with source median (41).
- Filled missing `City` with `Unknown`.
- Kept repeated `Order_ID` records for review.
- Added `Month` and `Sales_Check` analysis columns.

## SQL
Import the `Cleaned_Data` sheet as a SQLite table named `sales`, then run queries in `Task2_SQL_Queries.sql` one at a time. The workbook also includes query result sheets `Q1_Product` through `Q7_Age`.

## Important
- Review the outputs before submission.
- The SQL date function uses SQLite `strftime`; other database systems may need a different date function.
- The dashboard is a static mock-up, not a live interactive dashboard.
- You still need to upload the files to your public GitHub repository and record your own 5–7 minute walkthrough. Do not claim these steps are done until you complete them.
