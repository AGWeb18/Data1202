import pandas as pd 
from week8_helper import df_filter, get_top3_publisher

#   Set our file path to a variable
FILE_NAME = 'videogame/vgsales.csv'
COL_NAME = 'Platform'
l_to_filter = ['PC', 'PS4', 'N64']

#   Read the csv into a DataFrame
raw_df = pd.read_csv(FILE_NAME)

#   Call the function
l_publisher = get_top3_publisher(raw_df)

#   Filter DataFrame
top3_df = raw_df[raw_df['Publisher'].isin(l_publisher)] #   pandas .isin()

#   Save the dataframe
filtered_top3 = df_filter(top3_df, COL_NAME, l_to_filter)

#   Print Output
print(filtered_top3)

print(filtered_top3.sort_values(by='Global_Sales', ascending=False))



