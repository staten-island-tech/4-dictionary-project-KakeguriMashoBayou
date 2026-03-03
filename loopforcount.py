sentence = "happys is a test"
t = 0
s = 0
for letter in sentence: 
    if letter.lower() == "s": 
        s=+1
    elif letter == "t" or letter == "T":
        s= t+1
print (t)