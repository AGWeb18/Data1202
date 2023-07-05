#   How many games per platform
#   CREATE A FUNCTION TO DO THIS ****  
def num_games(_df, groupby_col, value_col):
    _games_df = _df.groupby([groupby_col])[value_col].count().reset_index()
    return _games_df