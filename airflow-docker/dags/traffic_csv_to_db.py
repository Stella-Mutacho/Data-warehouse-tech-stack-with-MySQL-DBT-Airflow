
import argparse
import os
import csv
from datetime import timedelta, datetime

from model import Connection, TrafficFlow
import config

# def get_yesterday_date(fetch_date):
#     return datetime.strptime(fetch_date, '%Y-%m-%d').date() - timedelta(1)

# def get_file_path(fetch_date):
#     yesterday = get_yesterday_date(fetch_date)
#     filename = "tomtom_{}.csv".format(yesterday)
#     return os.path.join(config.CSV_FILE_DIR, filename)

def main(fetch_date, db_connection):
    # yesterday = get_yesterday_date(fetch_date)
    # filename = get_file_path(fetch_date)
    data_insert = []
    
    with open('20181024_d1_0830_0900.csv', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            traffic_data = TrafficFlow(id=row['id'],
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