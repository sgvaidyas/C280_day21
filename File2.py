#works only with rb => read binary
f = open("aaaa", "rb")

f.seek(-14, 2)
# prints current position
print(f.tell())

# Converting binary to string and printing
print(f.readline().decode('utf-8'))

f.close()
