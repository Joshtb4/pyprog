inp = open("text.txt", "r")
data = inp.readlines()
# for line in data:
#    if "3 in line":
#         print(line,end="")
inp.close()
  # file = inp

out = open("outfile.txt", "w") 
for line in data:
    if not "3" in line:
        out.writelines(line.upper())
    out.close()
    