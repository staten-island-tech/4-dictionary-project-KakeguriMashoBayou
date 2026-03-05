def magnus(word):


  count = 0
state = 0
if state == 0 and char.upper() == 'H':
    state = 1
elif state == 1 and char.upper() == 'O':
    state = 2
elif state == 2 and char.upper() == 'N':
    state = 3
elif state == 3 and char.upper() == 'I':
            count += 1
            state = 0
    print(count)
magnus("honihonihonihonihoni")
