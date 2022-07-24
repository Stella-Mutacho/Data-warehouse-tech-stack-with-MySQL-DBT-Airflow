
import argparse
import os
import csv
from datetime import timedelta, datetime
from model import Connection, TrafficFlow
import config

def get_file_path(fetch_date):
    """
    This function constructs a filename to be used 
    Params:
        fetch_date: str
            The date the data was downloaded from the pNeuma API
    Returns:
        filepath: os.Path
            The path to the file
    """
    filename = "traffic_flow_{}.csv".format(fetch_date)
    return os.path.join(config.CSV_FILE_DIR, filename)

def main(fetch_date, db_connection):
    """
    Loads the data from csv file to the the database
    Params:
        fetch_date: str
            The date the data was downloaded from the web.
            This is used to construct the file path
        db_connection: str
            The database connection string
    """
    filename = get_file_path(fetch_date)
    data_insert = []
    
    with open(filename, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            traffic_data = TrafficFlow(
                                track_id=row['track_id'],
                                vehicle_types=row['vehicle_types'],
                                traveled_d=row['traveled_d'],
                                avg_speed=row['avg_speed'],
                                trajectory=row['trajectory'])
            data_insert.append(traffic_data)

    connection = Connection(db_connection)
    session = connection.get_session()
    session.bulk_save_objects(data_insert)
    session.commit()
    session.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, type=str)
    parser.add_argument("--connection", required=True, type=str)
    args = parser.parse_args()
    main(args.date, args.connection)