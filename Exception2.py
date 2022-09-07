try:
    s = input("Enter the string ")
    ind = int(input("Enter the index = "))
    print("We have '{}' at the index={}".format(s[ind],ind))
except IndexError:
    print("Index out of range")
print("-----------------------------")
