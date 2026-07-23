# while loop
#it works while condition is true
a=1
while a < 10:
    print(a)
    a+=1
print('its completed')
b=2
#while True:
#    print('g')#it creates infinity because its true and while true it works

#c=2
#while True:
b='supra'
guess=''

limit=0
out_of_guess=False
while b!=guess and not(out_of_guess):# it goes from while and starts and reches upto if 
    #checks if 0<3 yes works and execute upto limit becomes 1 and it goes straight upto while to check
    #and now 1 <3 yes works again
    if limit < 3:
        guess = input('enter a name')
        
        
        limit += 1
    else:
        out_of_guess = True
        print('its out of guess')
if out_of_guess:#this time it is out of while and becomes it out_of_guesses is true 
    print('you are out of guess')
else:
    print("its correct")
    

