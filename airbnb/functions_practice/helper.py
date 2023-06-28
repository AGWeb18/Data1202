import pandas as pd

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