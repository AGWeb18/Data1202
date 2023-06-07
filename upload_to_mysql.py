#   Load data from CSV to MySQL 
import pandas as pd
from sqlalchemy import create_engine


_table_name = "product2023" # Enter table name here
_uname = 'root' # Enter username here
_pw = '' # Enter password here
_db_name = 'product' #  enter database name here
_file_name = 'Argos_UK_Scraped_Product_Info-Batch2.csv' # Enter file name here


########################################

# Create an engine to the MySQL database
engine = create_engine('mysql+mysqlconnector://{}:{}@localhost/{}'.format(_uname, _pw, _db_name), echo=False)

# Read the CSV file
data = pd.read_csv(_file_name, encoding='latin-1')

# Write the data from the CSV file to the database
data.to_sql(_table_name, con=engine, index=False, if_exists='replace')
