# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock}: {quantity} shares = ${investment}")
    else:
        print("Stock not found.")

print(f"\nTotal Investment Value: ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}\n")

print("Result saved to portfolio.txt")
