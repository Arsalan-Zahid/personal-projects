import pandas as pd
import sys
import datetime
from os import path
import time

#get data
argv = sys.argv
msg = argv[1]

#get time data
current_time = datetime.datetime.now()
unix_time = int(time.mktime(current_time.timetuple()))

#get df, append, save
df_path = path.join(path.dirname(__file__), 'distractions.csv')
distractions_df = pd.read_csv(df_path, index_col=[0])

#append time
distractions_df.loc[unix_time, 'timestamp'] = current_time
distractions_df.loc[unix_time, 'msg'] = msg

#save it
distractions_df.sort_index(inplace=True, ascending=False)
distractions_df.to_csv(df_path, index=True)