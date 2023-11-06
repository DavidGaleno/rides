import sqlite3
import csv

def csv_to_sqlite(csv_file, sqlite_db, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Open the CSV file and read the column names
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        columns = csv_reader.fieldnames

        # Insert data from the CSV file into the SQLite table
        insert_sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(["?"] * len(columns))})'
        for row in csv_reader:
            cursor.execute(insert_sql, [row[column] for column in columns])

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Specify the path to your CSV file and the SQLite database file
csv_file = 'df_stations.csv'
sqlite_db = 'db.sqlite3'
table_name = 'rides_station'

# Call the csv_to_sqlite function
csv_to_sqlite(csv_file, sqlite_db, table_name)