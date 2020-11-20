import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder

### The features "player1", "player2" and "Tournament" are treated differently
### from the other features.

def categorical_features_encoding(cat_features):
    """
    simple one-hot encoding
    :param cat_features:
    :return:
    """
    cat_features=cat_features.apply(preprocessing.LabelEncoder().fit_transform) #类别编码成0 - n_class -1
    ohe = OneHotEncoder()
    cat_features=ohe.fit_transform(cat_features) # 独热向量编码
    cat_features=pd.DataFrame(cat_features.todense())
    cat_features.columns=["cat_feature_" + str() for i in range(len(cat_features.cololumn))]
    cat_features=cat_features.astype(int)
    return cat_features


def features_players_encoding(data):
    """
    Encoding of the players .
    The players are not encoded like the other categorical features because for each
    match we encode both players at the same time (we put a 1 in each row corresponding
    to the players playing the match for each match).
    """
    winners=data.Winner
    losers=data.Loser
    le = preprocessing.LabelEncoder()
    le.fit(list(winners)+list(losers)) # 合并两个list，python的动态类型很方便
    winners=le.transform(winners)
    losers=le.transform(losers)
    encod=np.zeros([len(winners),len(le.classes_)])
    for i in range(len(winners)):
        encod[i,winners[i]]+=1
    for i in range(len(losers)):
        encod[i,losers[i]]+=1
    columns=["player_"+el for el in le.classes_]
    players_encoded=pd.DataFrame(encod,columns=columns)
    return players_encoded

def features_tournaments_encoding(data):
    """
    Encoding of the tournaments .
    """
    tournaments=data.Tournament
    le = preprocessing.LabelEncoder()
    tournaments=le.fit_transform(tournaments)
    encod=np.zeros([len(tournaments),len(le.classes_)])
    for i in range(len(tournaments)):
        encod[i,tournaments[i]]+=1
    columns=["tournament_"+el for el in le.classes_]
    tournaments_encoded=pd.DataFrame(encod,columns=columns)
    return tournaments_encoded
