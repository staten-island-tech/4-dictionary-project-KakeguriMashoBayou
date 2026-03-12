coins = 48
machine = 3
machine2 = 10
machine3 = 4
played = 0 
type = 1
while coins > 0:
    coins = coins - 1
    played = played + 1
    if type == 1:
        machine = machine + 1
    if machine == 35:
        coins = coins + 30
    type = 2
    elif type == 2:
    
