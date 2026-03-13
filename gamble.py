coins = 48
machine = 3
machine2 = 10
machine3 = 4
played = 0 
type = 1
while coins > 0:
    coins = coins - 1
    played = played + 1

    if type ==1:
        machine = machine + 1
        type =2 
        if machine == 35:
            coins = coins + 30
            machine = 0
    elif type == 2:
        machine2 = machine2 + 1
        type = 3
        if machine2 == 100:
            coins = coins+60
            machine2 = 0
    elif type == 3:
        machine3=machine3 + 1
        type = 1
        if machine3 ==10:
            coins = coins + 9
            machine3=0
print("Martha plays", played, "times before going to the streets and beg")                                                                        