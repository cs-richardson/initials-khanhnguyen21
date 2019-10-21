'''
This program outputs one's initial names character
By Khanh Nguyen 
'''
name = input('Name:')
findSpace = False
total = ''
loopTimes = len(name)
letter = ''
for x in range(loopTimes):
    letter  = name[:1]
    name = name[1:]
    if letter != ' ' and findSpace == True:
        findSpace = True
    elif letter != ' ' and findSpace == False:
        findSpace = True
        total = total + letter.capitalize()
    else:
        findSpace = False
print(total)
    
    
