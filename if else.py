#so in order to understand true i will explain
is_short=True
is_fat=False
if is_short or is_fat:
    print('its okay')#so for using or either value should be true and its not like true or false just
    #watch condition like is_short and is_fat means its true and afteer check wether value given is_short=true
    # value givem is_fat=true? 
if is_short and is_fat:
    print('you see its eitheer short or fat')#only prints when is_short and is_fat are true on both condition
if is_short and not(is_fat):
    print('its short but also fat')#it prints because not(is_fat) i.e false and given is_fat also false

else:
    print('its not opkay')