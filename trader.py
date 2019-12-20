import yfinance as yf
import pandas as pd
from datetime import date
from datetime import datetime

class trader:
    def __init__(self):
        self.stocks = {}            #{name_date_time : [num of stocks, price stocks bought at]}
        self.reserve = 50
        self.net = 0

    def buy(self, stock , ammount):
        key = stock + "_" + str(date.today()) + "_" + str(datetime.now().time())
        if (stock not in self.stocks): 
            buyprice = round((yf.Ticker(stock).info["ask"] + yf.Ticker(stock).info["bid"]) / 2, 2 ) #buy price
            if (self.reserve > ammount * buyprice):
                self.stocks[key] = [ammount , buyprice] 
                self.reserve -= ammount * buyprice
                print("bought " + str(ammount) + " stock(s) for " + key)
            else:
                print("not enough money")
        else:
            print("Already owned stocks")

    def sell(self, key, ammount):
        if key in self.stocks:
            if (self.stocks[key][0] >= ammount):
                self.stocks[key][0] -= ammount
                stockName = key[:key.index("_")]
                sellprice = round((yf.Ticker(stockName).info["ask"] + yf.Ticker(stockName).info["bid"]) / 2, 2 )
                self.reserve += sellprice * ammount 
                if (self.stocks[key][0] == 0):
                    del self.stocks[key]
                    print("All stocks of " + key + " sold")
                else:
                    print(str(ammount) + " stock(s) sold. " + str(self.stocks[key][0]) + " left for " + key)
            else:
                print("cant sell " + str(ammount) + " stock(s). Only " + str(self.stocks[key][0]) + " owned")
        else:
            print("Key " + key + " not found")
        
        
    def stocksByName(self, stock):
        matches = []
        for i in self.stocks:
            if i.startswith(stock):
                matches.append(i)

        return matches

    def printTraderDetails(self):
        print()
        print()
        print("Reserve=" + str(self.reserve) + "      Net="+str(self.reserve-50))
        print("---------=Current Stocks=--------")
        for i in self.stocks:
            print(i, " --Stocks Held = " + str(self.stocks[i][0]) + " --Bought At = " + str(self.stocks[i][1]))
        print()
        print()

