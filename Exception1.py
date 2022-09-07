try:
    num1 = float(input("Enter the val of num1  = "))
    num2 = float(input("Enter the val of num2  = "))
    res = num1/num2
    print("Result = ",res)
except ZeroDivisionError:
    print("Denominator is 0 ==> Divide by zero error")
except ValueError:
    print("the dataype for the input is int -> supplied value doesnt match")
except:
    print("Generic error")

print("I m just here ")
print(" and me too !!!")

