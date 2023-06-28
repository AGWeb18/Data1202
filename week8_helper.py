#   Questions
# Retrieve all data from the top 3 Publishers (in Global_Sales)

def get_top3_publisher(_df):

    #   First --- IDENTIFY who the top 3 Publishers are. 
    _publishers = _df.groupby(['Publisher'])['Global_Sales'].sum().reset_index() # Perform Groupby
    _publishers = _publishers.sort_values(['Global_Sales'], ascending=False)[:3] # Keep top 3 rows. 
    return _publishers['Publisher'].to_list() # pandas to_list()


#   Create a function
def df_filter(_df, _col_name, *_value):
    """
    (function) def df_filter(
    _df: Any,
    _col_name: Any,
    *_value: List
    )   Returns: Dataframe
    """
    return _df[_df[_col_name].isin(*_value) ] # Applies a filter to a dataframe