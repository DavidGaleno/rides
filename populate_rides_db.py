import os, django,sqlite3,csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from rides.models import Ride, Station

def csv_to_sqlite(csv_file, sqlite_db, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Open the CSV file and read the column names
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        columns = csv_reader.fieldnames

        # Insert data from the CSV file into the SQLite table
        for row in csv_reader:
            # Get the station objects based on the identifiers
            station_start = Station.objects.get(station=row['station_start'])
            station_end = Station.objects.get(station=row['station_end'])

            # Create a new Ride instance with the station objects
            if(row['ride_late'] == '0.0'): row['ride_late'] = 0
            elif(row['ride_late'] == '1.0'): row['ride_late'] = 1
            else: row['ride_late'] = None
            ride = Ride(
                user_gender=row['user_gender'],
                user_birthdate=row['user_birthdate'],
                user_residence=row['user_residence'],
                ride_date=row['ride_date'],
                time_start=row['time_start'],
                time_end=row['time_end'],
                station_start=station_start,
                station_end=station_end,
                ride_duration=row['ride_duration'] if row['ride_duration'] != '' else None, 
                ride_late=row['ride_late'])
            

            # Save the Ride instance to the database
            ride.save()

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Specify the path to your CSV file and the SQLite database file
csv_file = 'df_rides.csv'
sqlite_db = 'db.sqlite3'
table_name = 'rides_ride'

# Call the csv_to_sqlite function
csv_to_sqlite(csv_file, sqlite_db, table_name)