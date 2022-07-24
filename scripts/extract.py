from ast import Try
import pandas as pd
import sys
import logging
import syslog
sys.path.append('../')


logger = logging.getLogger()
formatter= logging.Formatter('%(asctime)s -%(lineno)s -%(levelname)s-%(message)s')
logger.setLevel(logging.DEBUG)
fhandler= logging.FileHandler(filename='../airflow-docker/logs/notebook.log', mode='w')
fhandler.setFormatter(formatter)
fhandler.setLevel(logging.INFO)
logger.addHandler(fhandler)

def getDf(filepath):
    data= pd.read_csv(filepath)

    columns = data.columns[0].split(";")[:4]
    columns.append("trajectory")
    columns[1] = "types"
    for i in range(len(columns)):
        columns[i] = columns[i].strip()
    logging.info(columns)


    track_ids = []
    types = []
    traveled_d = []
    avg_speeds = []
    trajectories = []

    for r in range(len(data)): 
        row = data.iloc[r,:][0].split(";")
        row_p1 = row[:4]
        row_p2 = row[4:]
        trajectory = ','.join(row_p2)
        
        track_ids.append(row_p1[0])
        types.append(row_p1[1])
        traveled_d.append(row_p1[2])
        avg_speeds.append(row_p1[3])
        trajectories.append(trajectory[1:])

    data_dict= {columns[0]:track_ids, columns[1]:types, columns[2]:traveled_d, columns[3]:avg_speeds,columns[4]:trajectory}

    def dataframe(data_dict):
        df= pd.DataFrame(data_dict)

        try:
            df.head()
            
        except:
            print('No dataframe')
    
    def save(df, filename):
        df.to_csv(filename)
        syslog.LOG_DEBUG('Successfully saved')

