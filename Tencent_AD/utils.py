from datetime import datetime,timedelta
import pandas as pd
import numpy as np
import pickle,os,time,gc,re,math
import matplotlib.pylab as plt
import logging

logging.basicConfig(level=logging.INFO)

def getMonoScore(samplefilename,submissionfilename):
    names = ['sample_id', 'ad_id', 'target_conversion_type', 'charge_type', 'bid']
    test_samplefile = pd.read_csv(samplefilename,delimiter='\t', \
                                  header=None, names=names,dtype={'smaple_id':int,
         'ad_id': int, "target_conversion_type": int, 'charge_type': int, "bid": int},
                                  usecols=['sample_id', 'ad_id', 'bid'])

    test_sampledf = pd.DataFrame(test_samplefile)

    test_sampledf_result = pd.read_csv(submissionfilename,sep=",",header=None, names=["sample_id", "exp_num"])

    test_sampledf_resultdf = pd.DataFrame(test_sampledf_result)

    # left join two datasets
    test_sampledf = pd.merge(test_sampledf,test_sampledf_resultdf,how='left', left_on='sample_id',right_on='sample_id' )
    test_sampledf.sort_values(by=["ad_id","bid"], inplace=True) # 排序

    standard = test_sampledf.groupby(by='ad_id').head(1) # 这里groupby以后每组取第一行
    standard.rename(columns={'sample_id': 'base_sample_id', 'bid': 'base_bid', 'exp_num': 'base_exp_num'}, inplace=True)

    test_sampledf = pd.merge(test_sampledf, standard, how='left',left_on='ad_id',right_on='ad_id')
    test_sampledf['score'] = test_sampledf.apply(
        lambda x: (
           # ((x['base_exp_num'] - x['exp_num']) * (x['base_bid'] - x['bid'])) /
           # abs((x['base_exp_num'] - x['exp_num']) * (x['base_bid'] - x['bid']))
           x['base_exp_num'] - x['exp_num'] # testing
        )
       , axis=1
    )
    # 有了group以后，第一个mean是求组内均值，然后再求总共的均值
    #monoscore = test_sampledf.groupby(by='ad_id')['score'].mean().mean() # 组内
    t01 = test_sampledf.groupby(by='ad_id')
    t02 = t01['score']
    t03 = t02.mean()
    monoscore = t03.mean()
    print("score: " + str(60 * (monoscore + 1) /2 ))


def win_ad(x):
    count = 0
    win_ads = []
    ads_list = x.split(";")
    #print(ads_list)
    for per_ad in ads_list:
        per_ad_attribute = per_ad.split(",")
        if per_ad_attribute[-1] == "1":
            win_ads.append(','.join(per_ad_attribute))
    return '|'.join(win_ads)

def extract_test_track_log_num_of_opponets(track_log_df):
    pass




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
#df = tmp(samplefilename)
#df.groupby('ad_id')
