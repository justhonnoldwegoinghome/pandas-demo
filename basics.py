import pandas as pd


numbers = pd.read_csv("numbers.csv")
stats = pd.read_csv("stats.csv")

# ====================================== #
#                 Create                 #
# ====================================== #
pd.DataFrame({"A": 1, "B": [1, 2, 3]})
pd.Series([1, 2, 3, 4])


# ====================================== #
#                  Read                  #
# ====================================== #
numbers["player"]  # returns series
numbers[["player", "team"]]
numbers[numbers["number"] > 20]
numbers.loc[numbers["number"] > 20, "player"]


# ====================================== #
#                  Update                #
# ====================================== #

## -----------------------------------------------------------------------------
## Combining dataframes
## -----------------------------------------------------------------------------

### Merge
pd.merge(
    numbers,
    stats,
    how="inner",
    on=None,
    left_on="player",
    right_on="player",
    left_index=False,
    right_index=False,
    sort=True,
)

## -----------------------------------------------------------------------------
## Grouping within dataframe
## -----------------------------------------------------------------------------
grouped = stats.groupby("team")  # TODO: read about `group_keys` argument

for group, group_df in grouped:
    print(group)
    print(group_df)


## -----------------------------------------------------------------------------
## Reshaping dataframe
## -----------------------------------------------------------------------------

## -----------------------------------------------------------------------------
## Calling function on dataframe/grouped
## -----------------------------------------------------------------------------
"see df_funcs.py"
