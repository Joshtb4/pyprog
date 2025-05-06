# for i in range(1,101):
#     if i % 2 == 0:
#      print(i**2)

# while True:
     
#     temp = int(input("enter a temperature: "))

#     if temp >= 21:
#         print("turn heating off")
    
#     else:
#          print("turn heating on")









while True:
     
    temp = int(input("enter a temperature: "))
    time = int(input("enter a time"))
    
    if temp < 21 and time >=6 and time <=22:
        print("turn heating on")
    
    else:
         print("turn heating off")