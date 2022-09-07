f = open("aaaa", "r")

f.seek(22)
print(f.read(8))
print(f.tell())

print(f.readline())
f.close()
