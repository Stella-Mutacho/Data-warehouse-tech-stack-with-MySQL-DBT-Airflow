import argparse
from pathlib import Path

from model import Connection
import config


# Initialize Traffic_Flow Table
def main(db_connection):
    """
    This function creates the traffic_flow table in the postgres database
    Params:
        db_connection 
            The connection string to connect to the postgres database
    """
    Path(config.CSV_FILE_DIR).mkdir(parents=True, exist_ok=True)
    
    connection = Connection(db_connection)
    session = connection.get_session()
    session.execute('''CREATE TABLE IF NOT EXISTS traffic_flow (
    id SERIAL UNIQUE PRIMARY KEY, 
    track_id INT, 
    vehicle_types VARCHAR(30), 
    traveled_d DECIMAL, 
    avg_speed DECIMAL, 
    trajectory VARCHAR)''')
    session.commit()
    session.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--connection", required=True, type=str)
    args = parser.parse_args()
    main(args.connection)