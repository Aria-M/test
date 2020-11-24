from util.util_db2 import *
import pandas as pd
import copy
import re
import string
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import

def get_event_sentence ():
    db = SqlDateOp('finance', 'finance_db')
    sql = """SELECT `news_id`,`sentence`,`entity`,`events`,`user`,`check_result` FROM event_sentence_industry_gf WHERE `check_result` is not NULL """
    event_sentence = db.get_df_sql(sql)
    # industry_name_list = (db.get_df_sql(sql))['name'].values.tolist()
    print(event_sentence)
    return event_sentence

event_sentence=get_event_sentence()

event_sentence1=copy.deepcopy(event_sentence)   ##工作数据集
column=event_sentence.columns

index_df = pd.DataFrame({"events": event_sentence1['events'].tolist()})
index_df['events1']=index_df['events'].apply(lambda x:x.replace('[','').replace(']',''))
event_sentence1['events1']=copy.deepcopy(index_df['events1'])
event_sentence2=copy.deepcopy(event_sentence1)   ##工作数据集

#一行 变 多行
event_sentence3=event_sentence2.drop('events1', axis=1).join(event_sentence2['events1'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('events1'))




#
#
# str.split(index_df['events1'][6962],',')
# for event in str.split(index_df['events1'][6962],','):
#     print(event)
#
# global event_sentence2
# event_sentence2=copy.deepcopy(event_sentence1)   ##工作数据集
#
#
global temp
temp=pd.DataFrame()
y=2


def clean_events(x):
    global event_sentence
    global temp
    global y
    # temp = event_sentence2
    filter_words=','
    if filter_words not in x['events1'].tolist():
         return None
    if filter_words in x['events1'].tolist():

        events=str.split(x['events1'].tolist()[0], filter_words)
        for event in events:
            df=x
            y=3
            df['events1']=event
            # global temp
            # temp=event_sentence2.append(df)
            event_sentence2=event_sentence2.append(df)
         # return event_sentence2
        return None
         # return df

# for i in range(0,6965):
#     clean_events(event_sentence2[i:i+1])
#
#
clean_events(event_sentence2[6962:6963])
#
# event_sentence2[6962:6963].apply(lambda x:clean_events(x),axis=1)