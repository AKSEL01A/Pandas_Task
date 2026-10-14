import pandas as pd

# ==============================================================================
# Pre-defined Datasets for the Tasks
# These DataFrames are provided for testing and experimentation.
# DO NOT REMOVE THIS CODE
# ==============================================================================

# Dataset for Sub-task 1: Products and pricing
PRODUCTS_DF = pd.DataFrame({
    "product_id": [101, 102, 103, 104, 105],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "price": [899.99, 24.50, 49.90, 249.00, 79.99],
    "stock": [15, 120, 75, 30, 50]
})

# Dataset for Sub-task 2: Weather sensor data containing missing values (NaN)
WEATHER_DF = pd.DataFrame({
    "city": ["Rome", "Milan", "Naples", "Turin", "Florence"],
    "temperature": [22.5, None, 25.0, 18.0, None],
    "humidity": [55.0, 68.0, None, 72.0, 60.0]
})

# Dataset for Sub-task 3: Employee department salaries
EMPLOYEES_DF = pd.DataFrame({
    "employee_id": [1, 2, 3, 4, 5, 6],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "department": ["Engineering", "HR", "Engineering", "Sales", "HR", "Sales"],
    "salary": [75000.0, 52000.0, 82000.0, 61000.0, 54000.0, 64000.0]
})

# Datasets for Sub-task 4: Relational tables for merging
CUSTOMERS_DF = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "customer_name": ["Alice", "Bob", "Charlie", "Diana"]
})

ORDERS_DF = pd.DataFrame({
    "order_id": [501, 502, 503, 504],
    "customer_id": [1, 2, 1, 3],
    "amount": [120.50, 45.00, 310.00, 89.90]
})

# Dataset for Sub-task 5: Students and exam scores
STUDENTS_DF = pd.DataFrame({
    "student_name": ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas"],
    "score": [88, 95, 72, 91, 84, 78],
    "age": [20, 21, 19, 22, 20, 21]
})

# ==============================================================================
# Sub-task Functions (Check readme.md for full details)
# ==============================================================================

def filter_rows_above_threshold(df: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    """Sub-task 1: Filter rows where the specified column is strictly greater than threshold."""
    pass

def fill_missing_values(df: pd.DataFrame, fill_value: float) -> pd.DataFrame:
    """Sub-task 2: Replace all missing values (NaN/None) with fill_value."""
    pass

def calculate_group_mean(df: pd.DataFrame, group_col: str, value_col: str) -> pd.Series:
    """Sub-task 3: Calculate the mean of value_col grouped by group_col."""
    pass

def merge_dataframes(left_df: pd.DataFrame, right_df: pd.DataFrame, on_column: str) -> pd.DataFrame:
    """Sub-task 4: Perform an inner merge of left_df and right_df on on_column."""
    pass

def sort_and_select_top(df: pd.DataFrame, sort_by_col: str, n: int) -> pd.DataFrame:
    """Sub-task 5: Sort df in descending order by sort_by_col and return the top n rows."""
    pass

def main():
    print("Sub-task 1:\n", filter_rows_above_threshold(PRODUCTS_DF, "price", 100.0))
    print("Sub-task 2:\n", fill_missing_values(WEATHER_DF, 0.0))
    print("Sub-task 3:\n", calculate_group_mean(EMPLOYEES_DF, "department", "salary"))
    print("Sub-task 4:\n", merge_dataframes(CUSTOMERS_DF, ORDERS_DF, "customer_id"))
    print("Sub-task 5:\n", sort_and_select_top(STUDENTS_DF, "score", 3))

if __name__ == "__main__":
    main()
