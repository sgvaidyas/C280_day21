f = open('data', 'r+')
#replaces the first 9 chars with "new line "
f.write("new line ")
#stores the position 9 where we have the cursor in currpos
currpos = f.tell()

#just reads the remaining content of the line
x = f.readline()
print(x)
#cursor now is in second line so when u give
# f.read from the secondline till end of the file we read everything
# and store in extradata
extradata = f.read()
print("extradata = ",extradata)
#put cursor back to 9th pos from beginning
f.seek(currpos)
#rewrite the remaining content
f.write(extradata)
#say where the cursor is right now
print(f.tell())

f.close()
