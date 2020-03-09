from datetime import datetime,timedelta
import pandas as pd
import numpy as np
import pickle,os,time,gc,re,math
import matplotlib.pylab as plt
import logging

def tmp(samplefilename):
    names = ['sample_id', 'ad_id', 'target_conversion_type', 'charge_type', 'bid']
    test_samplefile = pd.read_csv(samplefilename, delimiter='\t', \
                                  header=None, names=names, dtype={'smaple_id': int,
                                                                   'ad_id': int, "target_conversion_type": int,
                                                                   'charge_type': int, "bid": int},
                                  usecols=['sample_id', 'ad_id', 'bid'])
    return test_samplefile

path = "D:/Data/tencent_ad/"
samplefilename = path + "Data/BTest/Btest_sample_bid.out"
submissionfilename = path + "submission.csv"
#getMonoScore(samplefilename,submissionfilename)
df = tmp(samplefilename)
print(df.head(5))
df2 = df.groupby('ad_id')['bid'].agg({'nums':'count'})
print(df2.head(5))
df3 = df.groupby('ad_id').agg({'bid':'count'}).reset_index()
print(df3.head(5))
df4 = df.groupby(['ad_id','bid']).agg({'sample_id':'count'}).reset_index()
print(df4.head(10))
print(df3.index[:5])
