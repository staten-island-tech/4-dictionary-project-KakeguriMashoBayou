store = [
    {"name": "cat",
    "price": 100000,
    "department": "tiktok",},


    {"name": "prosthetic hand",
    "price": 100000,
    "department": "human",},


    {"name": "pickle",
    "price": 10,
    "department": "food"}
    ]
cart = []
print("Hello welcome to the all tea all shade store")
for index, item in enumerate(store):
       print("item #:", index)
       print("Name:", item["name"])
       print("price:", item["price"])
       print("department:", item["department"])
buying = True
while buying:
       purchase = int(input("Choose something brah. Put in item #"))
       print("are done choosing", store[purchase]["name"])
       cart.append(purchase)
       check_out=(input("are you done or what? Yes or No:"))
       if check_out == "Yes":
              buying = False
       else:    
              buying = True
for thing in cart:
       print(store[thing]["name"], "$", cart[thing]["price"])
       


