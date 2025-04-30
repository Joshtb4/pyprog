people = [] #blank array
for i in range(3):#the for loop states that it wants to run 3 times through 
    people.append(input(f"please enter friend name: "))#asking python to add the input to the people blank array 

    print(people) #print the variable "people" storing the list 
add_more= input("do you want another person y/n : ")# after meeting the max range of 3 in the for loop, it asks the user for a yes or 
                                                    # and then repeats the input asking for name again
while add_more == "y":
    people.append(input(f"please enter friend name: "))
    add_more= input("do you want another person y/n : ")
print(people)



# # names = []
# names.append(input("name"))
# names.append(input("name"))
# names.append(input("name"))
 

