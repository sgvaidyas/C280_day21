try:
    fp = open("aaaa","r")
    content = fp.read(10)
    print(content)
    for i in range(len(content)):
        print(i , content[i])
    fp.close()
except FileNotFoundError:
    print("the file doesnt exist")
