import pandas as pd

#   USER-DEFINED VARIABLES
file_path = "AB_NYC_2019-ascii.csv"
host_path = "host_dim.csv"
city_name = "Manhattan"

#   DEFINING THE FUNCTIONS
def city_analysis(_file_path, _city_name):
    #   EXTRACT --- LOAD 
    #   Load into a dataframe
    raw_df = pd.read_csv(_file_path)

    #   Check for errors, check data quality
    # Fill NA of Reviews_per_month with -1 
    raw_df['reviews_per_month'] = raw_df['reviews_per_month'].fillna(-1)

    #  Fill NA of last_review with '1900-01-01'
    raw_df['last_review'] = raw_df['last_review'].fillna('1900-01-01')

    #   Change data type of last_review to date !!!!!!!!!!!!!

    #   TRANSFORM into insights 
    #   Filters
    #   Filter dataset for Manhattan
    city_df = raw_df[raw_df['neighbourhood_group']== _city_name]
    return city_df


def host_analysis(_host_path, _df):
    raw_host = pd.read_csv(_host_path)
    joined_df = pd.merge(left=_df, right=raw_host, on='host_id')
    #   More Transformations can go here *** 
    #   Only select columns
    #   Fiilter for Dates / host analysis
    return joined_df


#   CALLING THE FUNCTIONS
city_analysis_df = city_analysis(file_path, city_name)

host_df = host_analysis(host_path, city_analysis_df)


print(host_df)








# high_value_brooklyn = brooklyn_df[brooklyn_df['price'] > 150]

# #   CASE statement 
# #   if price between 0 - 100 "cheap"
# #   if price between 100 - 150 "moderate"
# #   if price between 150-200 "average"
# #   if price between 200+ "expensive"
# raw_df.loc[(raw_df['price'] <= 100), "price_group"] = "cheap"
# raw_df.loc[(raw_df['price'] >= 200), "price_group"] = "expensive"


# #   Drop/add Columns
# #   remove column "host_name"
# selected_cols = raw_df[['host_name', 'price_group','price','room_type', 'neighbourhood_group']]


# #   Aggregates = Group By 
# #   Whats the average price by room type by neighbourhood
# # print(selected_cols.groupby(['room_type', 'neighbourhood_group'])['price'].mean().reset_index())

# #   Perform JOINS (SQL) 
# # raw_df -- df1
# # df_host_dim  -- d2
# df_host_dim = pd.read_csv("host_dim.csv")


# #   INNER join in Python 
# df_inner = pd.merge(left=raw_df, right=df_host_dim, on="host_id", how='inner')
# print(len(df_inner))

# #   LEFT join in Python
# df_left = pd.merge(left=raw_df, right=df_host_dim, on="host_id", how='left')
# print(len(df_left))

# #   RIGHT join in Python
# df_right = pd.merge(left=raw_df, right=df_host_dim, on="host_id", how='right')
# print(len(df_right))


#   LOAD
#   Write the data to a table, or a view. 