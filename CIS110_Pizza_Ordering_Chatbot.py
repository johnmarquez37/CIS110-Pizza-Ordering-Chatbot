print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I am going to walk you through the order process. After answering each question please press the enter key")
username = input("\nEnter your name:  ")
if username.lower() == "john marquez":
    print(f"\nMy creator, {username}. Pleasure to serve you!")
else:  
        print(f"\nHello, {username}. Nice to meet you!")
size = input("\nWhat size do you want? Enter small, medium or large: ")
flavor = input("\nEnter the flavor of pizza: ")
crustType = input("\nWhat type of crust do you want: ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value: ")
quantity = int(quantity)
method = input("\nIs this carry out or delivery: ")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
total = (pizzaCost * quantity) * salesTax + deliveryFee
print(total)
print("_" * 10)
print(f"Thank you, {username}, for your order. ")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
if total >= 50:
    print("\nCongratulations! You've been awarded a $10 off coupon for your next order. ")
else:
    print("\nOrder over $50 you will receive a free $10 off coupon! ")
print("_" * 10)







