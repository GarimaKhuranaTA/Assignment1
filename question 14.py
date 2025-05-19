valid_currency_input = input("Enter valid currencies separated by commas: ")
valid_currency_str_list = valid_currency_input.split(",")

valid_currency = []
for val in valid_currency_str_list:
    valid_currency.append(int(val.strip()))
money = int(input("Enter the total money: "))

valid_currency.sort(reverse=True)

for note in valid_currency:
    if money >= note:
        count = money // note
        print(str(note) + "-" + str(count))
        money -= note * count
