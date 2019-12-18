import tensorflow as tf
from tensorflow import keras
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters


import trader

register_matplotlib_converters()
#msft = yf.Ticker("MSFT")
#msftHist=msft.history(period="max")

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


#print(msftHist.loc["2000-01-01":"2019-12-16", "Open":"Close"])
#plt.plot(msftHist.loc["2000-01-01":"2019-12-16", "Open":"Close"])
#plt.show()

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

