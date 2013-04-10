# -*- coding: utf-8 -*-

#TODO コインの種類とコインの数はクラスか連想配列にする
coins = [1, 5, 10, 50, 100, 500]
num   = [3, 2, 1,  3,  0,   2  ]

#TODO 設定金額は引数として渡せるようにしてあげる
Total = 620

def solve(money):
    ans = 0

    #TODO rangeで指定している幅はコインの種類に依存するのでべた書きしない
    for idx in range(5, 0, -1):
        t = min(money/coins[idx], num[idx])
        money -= t * coins[idx]
        ans += t

    print ans

def __main__():
    solve(Total)

__main__()
