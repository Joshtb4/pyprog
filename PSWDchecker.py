inp = open("users.csv", "r")
data = inp.readlines()
inp.close()

print(data)

users = [{}]
for line in data:
    user = line.strip().split(",")
    users.update({user[0]:user[1]})
    

#print(users[1]) - username2,password2

name=input("username? ")
pwd=input("password? ")
if [name,pwd] in users:
    print("correct")
else:
    print ("incorect")

 
 
 
 
 
  # file = inp