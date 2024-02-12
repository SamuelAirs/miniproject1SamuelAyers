### INF601 - Advanced Programming in Python
### Samuel Ayers
### Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closingList = []

    for day in hist:
        closingList.append((day['Date'], day['Close']))

    print(closingList)

    return closingList

stocks = ["MSFT","AMZN","TSLA","AMD","AAPL"]

msftClosing = np.array(getClosing("MSFT"))


days = list(range(1, len(msftClosing)+1))

plt.plot(days, msftClosing)
plt.axis([1,10])
plt.xlabel("Days")
plt.ylabel("Closing Price")
plt.title("Closing Price for " + "MSFT")
plt.show()

