try:
    fp = open("aaaa","r")
    line = int(input("Enter no of lines you want to print"))
    try:
        content = fp.readlines()
        print("--------------")
        print(content)
        print("--------------")
        for i in range(line):
            print("Line {} = {}".format(i+1,content[i]),end="")
    except IndexError:
        print("Error")
    fp.close()
except FileNotFoundError:
    print("file does not exist")
except ValueError:
    print("the line num should be integer")
