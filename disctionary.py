item = [
    {"name": "cat",
    "price": "100000",
    "department": "tiktok",},


    {"name": "prosthetic hand",
    "price": "100000",
    "department": "human",},


    {"name": "pickle",
    "price": "10",
    "department": "food"}
    ]
for things in range(0,3):
    print(item[things]["name"],item[things]["price"],item[things]["department"]) 
price = 0
count = 0
buyer = input("what are you buying?" )
if buyer == "cat":
    print("cat")
    price += float(100000)
elif buyer == "prosthetic hand":
    print("prosthethic hand")
    price += int(100000)
elif buyer == "pickle":
    print("pickle")
while True:
    user = input("are you going to buy more? yes/no")
    if user == "no":
        print(buyer) 
        if count >=1:
            print(buy2)
        print("$", price)
        break
    else:       
        if user == "yes":
            count += 1
            buy2 = input("What do you want more brokie")
            if buyer == "cat":
                 print("cat")
                 price += float(100000)
            elif buyer == "prosthetic hand":
                print("prosthethic hand")
                price += int(100000)
            elif buyer == "pickle":
                print("pickle")
                price += int(10)