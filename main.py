# List of tickers and prices
stocks = {"CF": "6.1",
          "CFG": "9,4",
          "EXC": "20.4",
          "JPM": "11.0",
          "MTB": "13.3",
          "NVR": "10.3",
          "TMUS": "19.3",
          "URI": "12.9",
          "WBD": "14.9",
          "WDC": "11.0",
          }
# Obtain input from user and capitalize all inputs
ticker = input("Please enter the ticker/symbol you would like to know the current price of: ").upper()
stock = stocks.get(ticker)

# Show ticker and price unless unknown ticker entered
if stock:
    print("The current price of", ticker, " is ", stock, "!")
else:
    print("Sorry, this symbol is not in our list.")