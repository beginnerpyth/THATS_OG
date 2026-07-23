d={'l':'luv',
    'p':'puv',
    's':'suv',
    'k':'kuv'}
print(d['l'])
print(d.get('p'))
print(d.get('r','rossup'))#we can set the default value
print(d.keys())#it is a function thats why we add keys 
print(d.values())# its a function that why we add values
print(d.items())
for key,value in d.items():
    print(key,value)