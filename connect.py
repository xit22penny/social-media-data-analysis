__author__ = 'Xian Teng'

import mysql.connector
from mysql.connector import errorcode
import datetime
import pandas as pd

## connect to server
def connector(uname, pswd, hostname, databasename):
    try:
        cnx = mysql.connector.connect(user=uname, password=pswd, host=hostname,
                                database=databasename)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

### ==================== fetching data ============================ ###
## extract data within (start_time, end_time)
## start_date = datetime.date(2015,1,8)
def extract_dataframe(cursor, start_date, end_date):
    date_period = abs((end_date-start_date).days) ## the total days to extract
    table_name = "user_tweets_paris_"
    df_tweet = pd.DataFrame()
    print df_tweet.shape
    for delta in range(0, date_period):
        current_date = start_date + datetime.timedelta(days = delta)
        current_table_name = table_name + current_date.strftime("%Y%m%d")
        print("extracting data from "+current_table_name+"...")
        ## created_at, text, tweetID, user_id_str, in_reply_to_user_id_str, in_reply_to_status_id_str, lang, lat, lon, location
        ## sql_select = "SELECT created_at, tweetID, user_id_str, in_reply_to_status_id_str, in_reply_to_user_id_str, lang, lat, lon, text, location, screen_name FROM " + current_table_name +";"
        sql_select = "SELECT created_at, tweetID, user_id_str, lon, lat FROM " + current_table_name + " WHERE lat IS NOT NULL"
        print("=== " + sql_select + " ===")
        cursor.execute(sql_select)
        results = cursor.fetchall();
        df = pd.DataFrame([ij for ij in i] for i in results)
        df_tweet = df_tweet.append(df)
        print("=== dataframe shape for ", delta+1, " day: ", df_tweet.shape, "===")

    ## df_tweet.rename(columns = {0:'created_at', 1:'tweetID', 2:'user_id_str', 3: 'in_reply_to_status_id_str', 4: 'in_reply_to_user_id_str', 5: 'lang', 6: 'lat', 7:'lon', 8: 'text', 9:'location', 10:'screen_name'}, inplace = True)
    df_tweet.rename(columns = {0:'created_at', 1:'tweetID', 2:'user_id_str', 3: 'lon', 4: 'lat'}, inplace = True)
    return df_tweet

