fp = open("aaaa","rb")

content = fp.read()
print(content.decode('utf-8'))
x = fp.read()
print("X = ",x)
#fp.seek(-x ve ,2) =>  starts from eof and moves x bytes
fp.seek(-25,2)
print(fp.tell())
print(fp.readline().decode('utf-8'))
print(fp.tell())
#fp.seek(-x ve ,1) =>  starts from current and moves x bytes
fp.seek(-20,1)
print(fp.tell())
#fp.seek(x) =>  starts from beginning and moves x bytes
fp.seek(7)
print(fp.tell())
fp.close()
