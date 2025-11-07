# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 330}

portfolio = {}
total_investment = 0

while True:
    name = input("Enter stock name (or 'done' to finish): ").upper()
    if name == "DONE":
        break
    if name in stock_prices:
        qty = int(input(f"Enter quantity of {name}: "))
        portfolio[name] = qty
    else:
        print("Stock not found!")

# Calculate total investment
for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares\n")
    file.write(f"\nTotal Value: ${total_investment}")
print("Saved to portfolio.txt")

