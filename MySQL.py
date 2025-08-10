import mysql.connector
import csv
import pandas as pd
from datetime import datetime



# Load dataframe
df = pd.read_csv("covid_trade_data.csv")
# convert the date column to the correct format
df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))

# connect to the MySQL database
# 
cnx = mysql.connector.connect(user='root', password='bscs3945',
                              host='localhost',
                              database='covid_data')

# create the necessary tables in the database
cursor = cnx.cursor()

create_table_query = '''CREATE TABLE IF NOT EXISTS covid90_table (
                        Direction VARCHAR(255),
                        Year INT,
                        Date DATETIME,
                        Weekday VARCHAR(255),
                        Country VARCHAR(255),
                        Commodity VARCHAR(255),
                        Transport_Mode VARCHAR(255),
                        Measure VARCHAR(255),
                        Value BIGINT,
                        Cumulative BIGINT)'''
cursor.execute(create_table_query)

# convert the dataframe to a list of tuples
data = [tuple(row) for _, row in df.iterrows()]

# insert the data into the corresponding MySQL table
insert_query = '''INSERT INTO covid90_table (Direction, Year, Date, Weekday, Country, Commodity, Transport_Mode, Measure, Value, Cumulative)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
cursor.executemany(insert_query, data)
cnx.commit()

# export the data from the MySQL table to a .csv file
select_query = '''SELECT * FROM covid90_table'''
cursor.execute(select_query)
result = cursor.fetchall()
with open('covid90_table.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([i[0] for i in cursor.description])
    csvwriter.writerows(result)

# close the database connection
cursor.close()
cnx.close()