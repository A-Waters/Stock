import yfinance as yf
import pandas as pd


class trader:
    def __init__(self):
        self.stocks = {}
        self.buyStock = {}
        self.reserve = 50
        self.net = 0

    def buy(self, stock , ammount):
        if (stock not in self.stocks): 
            buyprice = round((yf.Ticker(stock).info["ask"] + yf.Ticker(stock).info["bid"]) / 2, 2 ) #buy price
            self.stocks[stock] = ammount
            self.buyStock[stock] = buyprice
            
        else:
            print("FOUND")