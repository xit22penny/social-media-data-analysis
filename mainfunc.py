

__author__ = 'Xian Teng'
# import createNetwork as cnet
# import TweetsTextMining as ttm
import pandas as pd
import datetime
import networkx
import re
from collections import Counter
import EventTree
import connect as cnt



language = 'en'
USER = 'xit'
PASS = 'xiantengpicso'
HOST = 'localhost'
DATABASE = 'db_paris_attack'
connector= cnt.connector(USER,PASS,HOST,DATABASE)
cursor = connector.cursor()
start_time = datetime.date(2015,11,1)
end_time = datetime.date(2015,11,30)

# df = cnet.extract_dataframe(cursor, start_time, end_time)
# df.to_csv("pairs_"+start_time.strftime("%Y-%m-%d")+".csv", index = False, encoding='utf-8')

# df = pd.read_csv("/Users/xianteng/Downloads/pairs_2015-11-01.csv")
# user_network = cnet.build_user_network(df)
# print("=== number of nodes: " + str(user_network.number_of_nodes()) + "\n")
# print("=== number of edges: " + str(user_network.number_of_edges()) + "\n")

# df = pd.read_csv("/Users/xianteng/Downloads/pairs_2015-11-01.csv")
# df.en = df[df['lang'] == 'en']
# ttm.term_frequency(df.en)

coordinate = [2.2, 2.5, 48.8, 49.0]
df = cnt.extract_dataframe(cursor, start_time, end_time)
df['lon'] = df['lon'].astype(float)
df['lat'] = df['lat'].astype(float)
df = df.loc[(df['lon'].between(2.2, 2.5, inclusive = True)) & df['lat'].between(48.8, 49.0, inclusive = True)]
print(df.shape)
df.to_csv("pairs_"+start_time.strftime("%Y-%m-%d")+".csv", index = False, encoding='utf-8')

# df = pd.read_csv("/Users/xianteng/Downloads/pairs_2015-11-13.csv")
# df['lon'] = df['lon'].astype(float)
# df['lat'] = df['lat'].astype(float)
# coords = df[['lon','lat']]
# X = coords.values
# Y = EventTree.find_centers(X, 10)



# >>> pd.DataFrame.from_dict(Y[1][0])
#           0          1
# 0  2.366670  48.800000
# 1  2.266260  48.801729
# 2  2.289133  48.801882
# 3  2.289133  48.801882
# 4  2.240045  48.801941
# 5  2.231780  48.805303
# >>> pd.DataFrame.from_dict(Y[1][1])
#           0          1
# 0  2.486002  48.803228
# 1  2.455430  48.803751
# 2  2.455430  48.803751
# 3  2.471072  48.805487
# >>> pd.DataFrame.from_dict(Y[0])
#           0          1
# 0  2.280504  48.802123
# 1  2.466983  48.804054
