import pandas as pd

pd.set_option('display.max_columns', 500)

file_path = "AB_NYC_2019-ascii.csv"

raw_df = pd.read_csv(file_path)



#   WHERE / FILTER in SQL vs Python 
sql_where_claus = """
SELECT 
    col1
    ,neighbourhood_group
    ,col3
FROM table
    
WHERE neighbourhood_group = 'Brooklyn'
"""

brooklyn_df = raw_df[raw_df['neighbourhood_group']=='Brooklyn']
# manhattan_df = raw_df[raw_df['neighbourhood_group']=='Manhattan']


#   GROUP BY 
sql_groupby = """
SELECT 
    neighbourhood
    ,host_name
    ,count(#reviews) as Numberofreviews
FROM table

GROUP BY neighbourhood
         ,host_name
"""
### -------------------
#   PYTHON
###
grped_neigh = raw_df.groupby(["neighbourhood"])['reviews_per_month'].count().reset_index()
grped_neigh = grped_neigh.sort_values(by='reviews_per_month', ascending=False)

#   RENAME COLUMN 
grped_neigh.columns = ['neighbourhood', '#ofRows']

#   FILTER
pop_neighbourhood = grped_neigh[grped_neigh['#ofRows'] > 500 ]

#   CASE WHEN 
#   > 2000 = VERY POPULAR
#   Between 1 - 2000 : Popular
#   Else Standard

sql_case_when = """
SELECT 
    CASE 
        WHEN #ofRows > 2000 THEN 'VeryPopular'
        WHEN #ofRows BETWEEN 1000 AND 2000 THEN 'Popular'
        ELSE 'Standard 
    END as 'newCol'
FROM table 
"""
print(pop_neighbourhood)

#   SYNTAX FOR CASE WHEN IN PYTHON 
# df.loc[(condition), 'NewCol'] = VALUE
# df.loc[((condition1) & (condition2)), 'NewCol'] = VALUE

pop_neighbourhood.loc[(pop_neighbourhood['#ofRows'] >= 2000), 'popularity'] = 'VERY Popular'

pop_neighbourhood.loc[((pop_neighbourhood['#ofRows'] > 1000) & (pop_neighbourhood['#ofRows'] < 2000)), 'popularity'] = 'Popular'

pop_neighbourhood.loc[(pop_neighbourhood['#ofRows'] <= 1000), 'popularity'] = 'Standard'

#   JOIN 
