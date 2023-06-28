

import pandas as pd
import matplotlib.pyplot as plt


file_name = 'vgsales.csv'


def business_problem(_topic, _image_file_name):
    raw_df = pd.read_csv(file_name)
    publisher_df = raw_df.groupby([_topic])[['Global_Sales', 'JP_Sales']].sum().reset_index()
    publisher_df = publisher_df.sort_values('Global_Sales', ascending=False)
    fig, ax = plt.subplots()
    ax.plot(year_analysis[_topic].values, year_analysis['Global_Sales'].values)  # Create a figure containing a single axes.
    plt.savefig(_image_file_name)
    return year_analysis

#   Called the function, grouped on "Year"
year_analysis = business_problem('Year', 'videoanalysis.png')
