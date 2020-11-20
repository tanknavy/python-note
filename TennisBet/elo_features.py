import panads as pd
import numpy as np


def compute_elo_ranking(data):
    players = list(pd.Searies(list(data.Winner) + list(data.Loser)).value_counts().index)  # 从两个栏位中合并唯一player列表
    elo = pd.Searies(np.one(len(players) * 1500, index=players))  # 球员长度，每个元素值是 1500， 索引名是player
    ranking_elo = [(1500, 1500)]

    for i in range(1, len(data)):
        w = data.iloc[i - 1, :].Winner  # 每一行的赢家name
        l = data.iloc[i - 1, :].Loser  # 每一行的输家
        elow = elo[w]  # 赢家的值, elo中一开始每个都是1500
        elol = elo[l]  # 输家
        pwin = 1 / (1 + 10 ** ((elol - elow) / 400))

        k_win = 32
        k_los = 32

        new_elow = elow + k_win * (1 - pwin)
        new_elol = elol - k_los * (1 - pwin)
        elo[w] = new_elow
        elo[l] = new_elol

        ranking_elo.append((elo[data.iloc[i, :].Winner], elo[data.iloc[i, :].Loser]))

        if i % 5000 == 0:
            print(str(i) + "matchs computed...")

        ranking_elo = pd.DataFrame(ranking_elo, columns=["elo_winner", "elo_loser"])
        ranking_elo["proba_elo"] = 1/(1 + 10 ** ((ranking_elo["elo_loser"] - ranking_elo["elo_winner"]) / 400))
        return ranking_elo
