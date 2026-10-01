# ApexPlanet Data Analytics Internship - Task 1

## Task
Data Immersion & Wrangling

## Dataset
Sales dataset containing 1000 records and 12 original columns.

## Work completed
- Inspected the dataset structure and data types.
- Converted `Order_Date` to date format.
- Standardized text fields by removing leading/trailing spaces.
- Identified missing values.
- Filled missing `Age` values with the median (41).
- Filled missing `City` values with the mode (Patna).
- Checked for exact duplicate rows.
- Flagged repeated `Order_ID` values instead of deleting records automatically.
- Validated that `Total_Sales = Quantity × Unit_Price`.
- Used the IQR rule to flag unusually high/low `Total_Sales` values.
- Created an analysis-ready Excel workbook.

## Important data-quality decisions
Repeated Order IDs were flagged because the rows are not exact duplicates and contain different transaction information. They should be reviewed rather than deleted automatically.

Total-sales outliers were flagged rather than removed because an unusually large sale can be a valid business transaction.

## Files
- `ApexPlanet_Task1_Cleaned_Data.xlsx`
- `task1_cleaning.py`

## Task 1 deliverables
The internship plan asks for a data dictionary, cleaning script, cleaned dataset, and a 3-5 minute LinkedIn walkthrough.
