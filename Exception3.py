try:
    a = eval(input("Enter the data = "))
    b = int(input("Enter the val = "))
    print(a/b)
except SyntaxError:
    print("provide some val")
except TypeError:
    print("Type error the divide operation is on mismatched types")
except NameError:
    print("variable does not exist/deleted or not defined properly")
except ValueError:
    print("value error wrt input ")
except ZeroDivisionError:
    print("Divide by zero!!!")
except:
    print("And an error is caught")
