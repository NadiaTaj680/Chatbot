import yfinance as yf              # importing necessary libraries
import requests
from prettytable import PrettyTable

API_KEY = "IWKGOLXSSYWM1C5E"                    # inserting free api key from alphavantage
BASE_URL= "https://www.alphavantage.co/query"

portfolio= {}

  # Function for fetching data of stocks

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return info["currentPrice"]
    except KeyError:
        print(f"Error: Could not fetch current price for {symbol}.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

 # Adding stock to the portfolio through symbol

def add_stock(symbol,shares,purchase_price):

    if symbol in portfolio:
        print(f"{symbol} is already in your portfolio.")
        return
    
    portfolio[symbol]= {
        "Shares":shares,
        "Purchase_Price":purchase_price
    }

    print(f"{symbol} added successfully to your portfolio.")

 # Removing stock from our portfolio through symbol

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} is removed successfully from your portfolio.")

    else:
        print(f"{symbol} not in your portfolio.")

    # Displaying portfolio

def Display_Portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return
     
    table= PrettyTable()
    table_columns=["Stock","Shares","Purchase Price($)","Current Price($)","Value($)","Gain/Loss(%)"]

    total_investment=0
    total_value=0

    for symbol,details in portfolio.items():
        current_price=fetch_stock_data(symbol)
        if current_price is None:
            print(f"Error fetching data for {symbol}.")
            continue

        shares= details["Shares"]
        purchase_price=details["Purchase_Price"]
        value= current_price*shares
        gain_loss=((current_price-purchase_price)/purchase_price)*100
        
        total_investment+=purchase_price*shares
        total_value+=value

        table.add_row([symbol,shares,purchase_price,f"{current_price:.2f}",f"{value:.2f}",f"{gain_loss:.2f}%"])
        

    print(table)
    print(f"Total Investment: ${total_investment:.2f}")
    print(f"Current Value: ${total_value:.2f}")
    print(f"Net Gain/Loss: ${total_value - total_investment:.2f}")


# Main loop
def main():
    print("Welcome to the Stock Portfolio Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add a Stock")
        print("2. Remove a Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter the number of shares: "))
            purchase_price = float(input("Enter the purchase price per share: "))
            add_stock(symbol, shares, purchase_price)
        elif choice == "2":
            symbol = input("Enter the stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == "3":
            Display_Portfolio()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


