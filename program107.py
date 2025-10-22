def RecArea(Num1,Num2):
    Area = Num1 * Num2
    return Area

def RecPara(Num1,Num2):
    Perimeter = 2*(Num1+Num2)
    return Perimeter

def main():
    Input1 = float(input("Enter length :"))
    Input2 = float(input("Enter width :"))

    result1 = RecArea(Input1,Input2)
    result2 = RecPara(Input1,Input2)

    print("Area of rectangle is : ",result1)
    print("Perimeter of rectangle is : ",result2)

if __name__ == "__main__":
    main()