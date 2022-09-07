f = open("aaa", "rb")

Lines = f.readlines()
f.close()
count = 0
print("\x1b[91m|\x1b[0m \x1b[93m     Today's Horoscope\x1b[91m     |\x1b[0m\n")
n = int(input("Which line number would u like to replace: "))
s = input("What would you like to replace it with: ")
# Strips the newline character
bigString = ""
for line in Lines:
    count += 1
    if count == n:
        bigString += s+"\n"
    else:
        bigString += str(line, 'utf-8')


f = open('aaaa','r+')
f.write(bigString)
f.close()
