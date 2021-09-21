lenght=int(input("Enter lenght of the list: "))
list_made=[] 

for loop in range(0,lenght):
    element=int(input("Enter Element: "))
    list_made.append(element)
print("You made this list {0}".format(list_made))
#bubble sorting
for i in range(lenght):             
    for j in range(0,lenght-i-1):                                   
        if list_made[j]>list_made[j+1]:                                                 
            list_made[j],list_made[j+1]=list_made[j+1],list_made[j]


print("\nThe sorted list: {0} ".format(list_made))
