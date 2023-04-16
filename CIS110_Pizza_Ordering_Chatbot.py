print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I am going to walk you through the order process. After answering each question please press the enter key")
username = input("\nEnter your name:  ")
print(f"\nHello, {username}. Nice to meet you!")
size = input("\nWhat size do you want? Enter small, medium or large: ")
flavor = input("\nEnter the flavor of pizza: ")
crustType = input("\nWhat type of crust do you want: ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value: ")
quantity = int(quantity)
method = input("\nIs this carry out or delivery: ")
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print(total)
print("_" * 10)
print(f"Thank you, {username}, for your order. ")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("_" * 10)






