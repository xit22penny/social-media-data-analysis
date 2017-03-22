
__author__ = 'Xian Teng'
### ============= Descriptions ========== ###
### Build various networks through social media data


import pandas as pd
import datetime
import networkx as nx
import re


## geocoding from text

### ==================== generate network ========================= ###
## find @mentions from text
def find_mentions(s):
    return re.findall(r'(?:@[\w_]+)', s) ## put all @mentions into a string joined by ','

## insert mention-based edges into graph
def insert_mention_edges(user_G, df):
    for i in range(0, len(df)):
        if(pd.isnull(df['text'][i]) == False):
            mentioned_username = find_mentions(df['text'][i])
            if(len(mentioned_username) > 0): 
                start_node = df['user_id_str'][i] ## start node
                for j in mentioned_username:
                    end_node = df[df['screen_name'] == j[1:]]['user_id_str']
                    if(len(end_node) > 0):
                        user_G.add_edge(start_node, end_node.iloc[0])

## build a user-user network by @mention @reply
def build_user_network(df_tweet):
    user_G = nx.Graph()
    reply_edge = df_tweet[['user_id_str','in_reply_to_user_id_str']]
    user_G.add_edges_from([tuple(x) for x in reply_edge.values]) ## add reply-based edges into user_G graph
    print("reply edges are finished.\n")
    insert_mention_edges(user_G, df_tweet) ## add mention-based edges into user_G graph
    print("mention edges are finished.\n")
    return user_G
### ==================== generate network ========================= ###



    
