list=['pam','jam','asm','kam']
print(list)
print(list[3])
list.append('gam')# we use this becaue () it is function and anything that is function is we use ()
print(list)
pist=[3,4,6,7,8,9,7]
list.extend(pist)#we use extend to join two list
print(list)
print(list.index('pam'))
print(list)
list.insert(2,"sam")
print(list)
list.remove("sam")
print(list)
list.pop()
print(list)
list.clear()
print(list)

def mama():
    a=int(input('enter a name'))
    for x in range(6):
        print(a-x)
        
mama()

