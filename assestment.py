V = input("Input:").upper()

count = 0

for letter in V:
    if letter == "H"and "O"and  "N" and "I":
        print(count +1)
        count = 0
    else:
        print(0)
