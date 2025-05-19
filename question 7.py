transactions = input("Enter transactions comma separated")
entries = [t.strip() for t in transactions.split(",")]

net_amount = 0
for entry in entries:
    action, amount = entry.split()
    amount = int(amount)
    if action == 'D':
        net_amount += amount
    elif action == 'W':
        net_amount -= amount

print(net_amount)
