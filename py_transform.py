from helper import city_analysis, host_analysis


#   USER-DEFINED VARIABLES
file_path = "AB_NYC_2019-ascii.csv"
host_path = "host_dim.csv"
city_name = "Brooklyn"


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