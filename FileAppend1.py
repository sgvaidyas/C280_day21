fp = open("mydata","a")

name = input("Enter name = ")
roll = input("Enter roll num = ")

s = "\n"+  name + " | " + roll
fp.write(s)

fp.close()
