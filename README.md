# Introduction

Pandas is a foundational Python library providing high-performance, easy-to-use data structures and data analysis tools for tabular and structured data. In this task, you are required to implement a set of data manipulation functions using the Pandas library.

# Instructions

- Fork this project on GitHub and make sure your repository is public. Then, import the project into your IDE (e.g., PyCharm).
- You cannot change the signature or rename the functions provided in `task.py`.
- You cannot interact with your peers: work individually and do your best.
- The features to implement are organized into a series of sub-tasks.
- Implement the functions one at a time, strictly following the order of the sub-tasks. Do not read upcoming sub-tasks in advance.
- A sub-task is considered completed when you are confident that the required functionality has been correctly implemented.
- Each time you complete a sub-task, commit and push your code to your repository.
- At the end of the assignment, ensure that the entire project has been pushed to your GitHub repository.

### Pre-defined Datasets

To make testing and experimentation immediate, several realistic DataFrames (`PRODUCTS_DF`, `WEATHER_DF`, `EMPLOYEES_DF`, `CUSTOMERS_DF`, `ORDERS_DF`, `STUDENTS_DF`) have been pre-defined at the top of `task.py` (outside of all functions). You can use them directly to inspect and test your implementations.

---

# Sub-tasks

Remember to read and implement the sub-tasks one at a time, strictly following the provided order. Do not proceed to the next sub-task until the current one is completed. Implement the required functions inside `task.py`.

---

## Sub-task 1 – Filter Rows by Condition

**Conditional filtering** (often called *boolean indexing*) allows you to select a subset of rows from a DataFrame based on values in one or more columns. Applying a comparison condition evaluates each row against specified criteria, retaining only rows that satisfy the condition while excluding the rest.

### Requirement

Implement the function:

```python
filter_rows_above_threshold(df: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame
```

This function receives:

- `df`: a Pandas `DataFrame`;
- `column`: the name of a numerical column (string);
- `threshold`: a numerical threshold value (float).

The function must return a new DataFrame containing only the rows where the value in `column` is strictly greater than `threshold` (`> threshold`).

### Examples

Given `df = pd.DataFrame({"product": ["A", "B", "C"], "price": [10.0, 25.0, 15.0]})`:

```python id="pd_f1"
Input: df, column = "price", threshold = 12.0
Output:
  product  price
1       B   25.0
2       C   15.0
```

```python id="pd_f2"
Input: df, column = "price", threshold = 20.0
Output:
  product  price
1       B   25.0
```

```python id="pd_f3"
Input: df, column = "price", threshold = 50.0
Output:
Empty DataFrame
Columns: [product, price]
Index: []
```

---

## Sub-task 2 – Fill Missing Values

In real-world data science, datasets frequently contain missing or unrecorded entries. In Pandas, missing numerical values are represented as `NaN` (*Not a Number*) or `None`. **Imputation** is the process of replacing missing data with substituted values, such as a designated constant, so that downstream algorithms and analyses can run without errors.

### Requirement

Implement the function:

```python
fill_missing_values(df: pd.DataFrame, fill_value: float) -> pd.DataFrame
```

This function receives:

- `df`: a Pandas `DataFrame` potentially containing missing values (`NaN`/`None`);
- `fill_value`: the numerical constant (float) to substitute for every missing value.

The function must return a DataFrame where all missing entries have been replaced with `fill_value`.

### Examples

Given `df = pd.DataFrame({"a": [1.0, None, 3.0], "b": [None, 5.0, None]})`:

```python id="pd_fm1"
Input: df, fill_value = 0.0
Output:
     a    b
0  1.0  0.0
1  0.0  5.0
2  3.0  0.0
```

```python id="pd_fm2"
Input: df, fill_value = -1.0
Output:
     a    b
0  1.0 -1.0
1 -1.0  5.0
2  3.0 -1.0
```

---

## Sub-task 3 – Group By and Aggregate (Mean)

The **split-apply-combine** strategy is a core data analysis pattern:

1. **Split**: partition the tabular data into groups based on key values in one or more categorical columns.
2. **Apply**: compute an aggregation summary function (e.g., mean, sum, count) independently on the numerical values within each group.
3. **Combine**: merge the results into an aggregate data structure.

In this sub-task, you will group rows by a categorical column and compute the arithmetic mean of a numerical column for each distinct category.

### Requirement

Implement the function:

```python
calculate_group_mean(df: pd.DataFrame, group_col: str, value_col: str) -> pd.Series
```

This function receives:

- `df`: a Pandas `DataFrame`;
- `group_col`: the name of the column containing group/category labels (string);
- `value_col`: the name of the numerical column whose mean should be calculated (string).

The function must return a `pd.Series` indexed by the unique values in `group_col`, containing the calculated mean of `value_col` for each group.

### Examples

Given `df = pd.DataFrame({"category": ["fruit", "vegetable", "fruit", "fruit"], "price": [3.0, 2.0, 5.0, 4.0]})`:

```python id="pd_gm1"
Input: df, group_col = "category", value_col = "price"
Output:
category
fruit        4.0
vegetable    2.0
Name: price, dtype: float64
```

Given `df = pd.DataFrame({"dept": ["IT", "HR", "IT"], "salary": [3000.0, 2500.0, 4000.0]})`:

```python id="pd_gm2"
Input: df, group_col = "dept", value_col = "salary"
Output:
dept
HR    2500.0
IT    3500.0
Name: salary, dtype: float64
```

---

## Sub-task 4 – Merge Two DataFrames

In relational data manipulation, related information is often distributed across multiple tables. An **inner join** (or merge) combines rows from two separate DataFrames (`left_df` and `right_df`) based on matching values in a shared key column. Only rows where the key value exists in **both** tables are included in the merged output.

### Requirement

Implement the function:

```python
merge_dataframes(left_df: pd.DataFrame, right_df: pd.DataFrame, on_column: str) -> pd.DataFrame
```

This function receives:

- `left_df`: the first Pandas `DataFrame`;
- `right_df`: the second Pandas `DataFrame`;
- `on_column`: the name of the common key column present in both DataFrames (string).

The function must perform an inner merge of both tables using the given key column and return the resulting merged DataFrame.

### Examples

Given:

```python
df1 = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
df2 = pd.DataFrame({"id": [1, 2, 4], "role": ["Admin", "User", "Guest"]})
```

```python id="pd_m1"
Input: left_df = df1, right_df = df2, on_column = "id"
Output:
   id   name   role
0   1  Alice  Admin
1   2    Bob   User
```

Given:

```python
customers = pd.DataFrame({"cid": [10, 20], "city": ["Rome", "Milan"]})
orders = pd.DataFrame({"cid": [10, 20, 30], "total": [150.0, 80.0, 45.0]})
```

```python id="pd_m2"
Input: left_df = customers, right_df = orders, on_column = "cid"
Output:
   cid   city  total
0   10   Rome  150.0
1   20  Milan   80.0
```

---

## Sub-task 5 – Sort and Select Top N

Sorting records based on one or more metrics is essential for ranking and filtering high-priority entries (e.g., top-performing products, highest test scores, largest transactions). In this sub-task, you need to sort a DataFrame in **descending order** according to a specified column and select the first $N$ rows (top $N$).

### Requirement

Implement the function:

```python
sort_and_select_top(df: pd.DataFrame, sort_by_col: str, n: int) -> pd.DataFrame
```

This function receives:

- `df`: a Pandas `DataFrame`;
- `sort_by_col`: the name of the column by which to sort the data (string);
- `n`: the number of top rows to retrieve (integer, $n \ge 0$).

The function must sort the DataFrame in **descending order** based on the values in `sort_by_col` and return the first `n` rows.

### Examples

Given:

```python
df = pd.DataFrame({
    "student": ["Emma", "Liam", "Olivia", "Noah"],
    "score": [88, 95, 72, 91]
})
```

```python id="pd_st1"
Input: df, sort_by_col = "score", n = 2
Output:
  student  score
1    Liam     95
3    Noah     91
```

```python id="pd_st2"
Input: df, sort_by_col = "score", n = 1
Output:
  student  score
1    Liam     95
```

```python id="pd_st3"
Input: df, sort_by_col = "score", n = 0
Output:
Empty DataFrame
Columns: [student, score]
Index: []
```
