### INF601 - Advanced Programming in Python
### Samuel Ayers
### Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import copy

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(price)

    return closingList

stocks = ["MSFT","AMZN","TSLA","AMD","AAPL"]

for stock in stocks:
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing)+1))

    #plots the graph
    plt.plot(days, stockClosing)

    #get min and max for y
    prices = getClosing(stock)
    prices.sort()
    lowPrice = prices[0]
    highPrice = prices[-1]

    #sets x axis min and max
    plt.axis([1,10,lowPrice-2,highPrice+2])

    #set graph labels
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    #shows the graph

    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    plt.show()