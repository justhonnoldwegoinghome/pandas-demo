import pandas as pd


stats = pd.read_csv("stats.csv")


"""
====================================================================
============= grouped.apply() vs. grouped.transform() ==============
====================================================================

Both methods no longer have 2 variants each. Each function call takes in 1 grouped_df.

grouped.apply(grouped_df): 
- output grouped_df can have different shape from intput grouped_df

grouped.transform(grouped_df): 
- output grouped_df cannot have different shape from intput grouped_df
"""

grouped = stats.groupby("team")


def apply_grouped_df(grouped_df):
    print("grouped_df")
    print("=========")
    print(grouped_df)
    return grouped_df["ppg"].mean()


grouped.apply(apply_grouped_df)


#
grouped = stats.groupby("team")[["ppg", "apg", "rpg"]]


def transform_grouped_df(grouped_df):
    print("grouped_df")
    print("=========")
    print(grouped_df)
    return (
        grouped_df - grouped_df.mean()
    )  # shape cannot be changed (grouped_df.mean() is just a scalar)


grouped.transform(transform_grouped_df)
