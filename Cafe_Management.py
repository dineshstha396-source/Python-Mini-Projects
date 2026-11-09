# Mini Project on Python 

# Cafe Management System 

# Menu of restaurant 

menu ={
    'Pizza':40,
    'Pasta':50,
    "Burger":60,
    'Salad': 70,
    'Coffee':80
}

# Greeting 

print("Welcome to Python Restaurant \nWe Have the following menu")

for key,value in menu.items():
    print(f"{key} : {value}")

order_total=0

flag=True 
li=[]

while flag:
   
    item=input("Enter the name of the item you want to order: ")
    if item in menu:
        order_total+=menu[item]
        li.append(item)
    else:
        print(f"We don't have the item avaiable.")

    another_order=input("Do you want to add another item ? (Yes/No)")

    if another_order.lower()=="no":
        flag=False
        
print(f'You have order the following items: ')
for i in li:
    print(i)
print(f"The total cost for your order is {order_total}.")