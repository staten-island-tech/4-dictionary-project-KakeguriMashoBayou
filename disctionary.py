item = [
    {"name": "chamoy kit",
    "price": "$100000",
    "department": "tiktok",},


    {"name": "prosthetic hand",
    "price": "$100000",
    "department": "human",},


    {"name": "pickle",
    "price": "$10",
    "department": "food"}
    ]
print(item[0]["name"],item[0]["price"],item[0]["department"])
print(item[1]["name"],item[1]["price"],item[1]["department"])
print(item[2]["name"],item[2]["price"],item[2]["department"]) 

price = 0
count = 0
buyer = input("what are you buying?" )
if buyer == "chamoy kit":
    print("chamoy kit")
    price += float(100000)
elif buyer == "prosthetic hand":
    print("prosthethic hand")
    price += int(100000)
elif buyer == "pickle":
    print("pickle")
    price+= int(10)
while True:
    user = input("are you going to buy more? yes/no")
    if user == "no":
        print(buyer) 
        if count >=1:
            print(buy2)
            

        if buyer == "chamoy kit":
            print("chamoy kit $100000")
        elif buyer == "prosthethic hand":
            print("prosthethic hand $100000")
        elif buyer == "pickle":
            print("pickle $10")
        break 
    else:
        if user == "yes":
            buy2 = input("are you going to buy more?")
            if buy2 == 