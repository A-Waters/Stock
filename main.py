import tensorflow as tf
from tensorflow import keras
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from datetime import date
import datetime



import trader

register_matplotlib_converters()


msft = yf.Ticker("MSFT")
msftHist=msft.history(period="max")



today = date.today()
one_year = today - datetime.timedelta(days=365)
two_year = today - datetime.timedelta(days=730)
ten_year = today - datetime.timedelta(days=3650)


print(msft.history(start=str(ten_year), end=str(ten_year)))

print("Today's date:", today)
print("1 years's date:", one_year)
print("2 years date:", two_year)
print("10 year date:", ten_year)
#print(msftHist.loc[str(today - ten_year):str(today), "Open":"Close"])
#plt.plot(msftHist.loc[str(today - ten_year):str(today), "Open":"Close"])
#plt.show()



def evalute(stock):
    msftHist=msft.history(period="max")
    open=0
    daliyhigh=0
    dailylow=0
    close=0
    change=0

    

    return






#print (msft.info)

'''
tradebot = trader.trader()

tradebot.buy("GE" , 3)

tradebot.printTraderDetails()

GE_STOCKS = tradebot.stocksByName("GE")
tradebot.sell(GE_STOCKS[0], 2)

tradebot.printTraderDetails()

tradebot.buy("GE" , 2)

GE_STOCKS = tradebot.stocksByName("GE")
tradebot.sell(GE_STOCKS[1], 2)
'''




#print(msftHist.loc["2000-12-01":"2019-12-16", "Open"])
#print(msftHist.loc["2000-12-01":"2019-12-16", "Close"])

#openNums = msftHist.loc["2000-12-01":"2019-12-16", "Open"]
#closeNums = msftHist.loc["2000-12-01":"2019-12-16", "Close"]





#print (openNums.size)
'''
for i in range(openNums.size):
    if (openNums[i] < closeNums[i]):
        goal[i] = 1
    else:
        goal[i] = 0

'''






'''
for i in msftHist.loc["2000-12-01":"2019-12-16", "Open":"Close"]:
    #print(msftHist.loc["2000-12-01":"2019-12-16", "Open":"Close"][i])
    print(i)
'''
'''
model = keras.models.Sequential([
    keras.layers.Dense(32,input_shape=(msftHist.loc["2000-01-01":"2019-12-16", "Open":"Close"].shape)),
    keras.layers.Activation('relu'),
    keras.layers.Dense(10),
    keras.layers.Activation('softmax')
])


model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

'''

