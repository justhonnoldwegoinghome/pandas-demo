import pandas as pd


numbers = pd.read_csv("numbers.csv")
stats = pd.read_csv("stats.csv")


"""
==========================================================
============= df.apply() vs. df.transform() ==============
==========================================================

Both methods have 2 variants each: 
- calling function on each col or or on each row

df.apply(): 
- each function call's input: array (from column or row)
- each function call's output: scalar or array of any length
- the output df will have the corresponding shape

df.transform(): 
- each function call's input: array (from column or row)
- each function call's output: array of same length as input array
- the output df will have same shape as input df
"""


def apply_col(col):
    print("Column")
    print("======")
    print(col)
    return col[10:] + 24  # shape changes to a smaller array


def apply_row(row):
    print("Row")
    print("======")
    print(row)
    return row.mean() % 2  # shape changes to a scalar


numbers[["index", "number"]].apply(apply_col)
numbers[["index", "number"]].apply(apply_row, axis=1)


def transform_col(col):
    print("Column")
    print("======")
    print(col)
    return col + 24  # maintains shape


def transform_row(row):
    print("Row")
    print("======")
    print(row)
    return row * 2  # maintains shape


numbers[["index", "number"]].transform(transform_col)
numbers[["index", "number"]].transform(transform_row, axis=1)
