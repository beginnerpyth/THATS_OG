

try:
        num=int(input(('enter a number ')))

        print(10/num)     
except ZeroDivisionError as e:
     print(e)
     num=int(input(('enter a number ')))
     
     print(10/num)
except ValueError as v:
       print('its a value error')
       num=int(input(('enter a number ')))
       print(10/num)
finally:
       
       print( 'its okay')
       num=int(input(('enter a number ')))
       print(10/num)
       
