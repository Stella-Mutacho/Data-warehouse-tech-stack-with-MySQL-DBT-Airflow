import os
import pandas as pd

class Extractor:

    def __init__(self):
        pass

    def load_csv(self, path):
        """
        Function to Load csv file.
        Args:
            path: location of csv file and its name.        
        Returns:
            df: dataframe.
        """
        df = pd.read_csv(path)
        return df

    def transform_raw_data(self, raw_data_df):
        """
            This function transforms the raw dataset extracted from the web into a dataframe that can be easily loaded the database    
            Returns: pd.DataFrame 
        """

        #Create empty lists to hold data in each column
        track_ids = []
        vehicle_types = []
        traveled_d = []
        avg_speeds = []
        trajectories = []
        for r in range(len(raw_data_df)): 
            row = raw_data_df.iloc[r,:][0].split(";")
            row_p1 = row[:4]
            row_p2 = row[4:]
            trajectory = ','.join(row_p2)        
            track_ids.append(row_p1[0])
            vehicle_types.append(row_p1[1])
            traveled_d.append(row_p1[2])
            avg_speeds.append(row_p1[3])
            trajectories.append(trajectory[1:])    
        columns = raw_data_df.columns[0].split(";")[:4]
        columns.append("trajectory")
        columns[1] = "vehicle_types"
        for i in range(len(columns)):
            columns[i] = columns[i].strip()
        data_dict= {columns[0]:track_ids, columns[1]:vehicle_types, columns[2]:traveled_d, columns[3]:avg_speeds,columns[4]:trajectory}

        df= pd.DataFrame(data_dict)
        print("dataframe successfully created")
        return df
    
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
        return os.path.join("~/data/", filename)

    def save_df(self, df, filename):
        df.to_csv(filename)
        print("Successfully saved the data to a csv file")

