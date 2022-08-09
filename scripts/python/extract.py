from ast import Try
import pandas as pd
import sys
import logging
import syslog
sys.path.append('../')


logger = logging.getLogger()
formatter= logging.Formatter('%(asctime)s -%(lineno)s -%(levelname)s-%(message)s')
logger.setLevel(logging.DEBUG)
fhandler= logging.FileHandler(filename='../../airflow_/logs/extract.log', mode='w')
fhandler.setFormatter(formatter)
fhandler.setLevel(logging.INFO)
logger.addHandler(fhandler)

class Extractor:

    def __init__(self):
        pass

    def load_csv(self, path):
        """
        a function to load csv file.
        Args:
            path: location of csv file and its name.
        
        Returns:
            df: dfframe.
        """
        df = pd.read_csv(path)
        return df

    def getDf(self, df):

        columns = df.columns[0].split(";")[:4]
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

        for r in range(len(df)): 
            row = df.iloc[r,:][0].split(";")
            row_p1 = row[:4]
            row_p2 = row[4:]
            trajectory = ','.join(row_p2)

            track_ids.append(row_p1[0])
            types.append(row_p1[1])
            traveled_d.append(row_p1[2])
            avg_speeds.append(row_p1[3])
            trajectories.append(trajectory[1:])

        df_dict= {columns[0]:track_ids, columns[1]:types, columns[2]:traveled_d, columns[3]:avg_speeds,columns[4]:trajectory}
        df= pd.dfFrame(df_dict)
        syslog.LOG_DEBUG('Successfully created dataframe')
        return df

    def save(self,df, filename):
        df.to_csv(filename)
        syslog.LOG_DEBUG('Successfully saved')

