user = input("sentence: ").upper()
char_to_count = "T"
count = user.count(char_to_count) 
print(count)
count2 = user.count(char_to_count)
char_to_count2 = "S "
print(count)

if count >= count2:
    print("Proabably English text")
else:
    print("Probably French text")