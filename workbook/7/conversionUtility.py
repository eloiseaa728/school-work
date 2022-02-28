def main():
    complete = False
    while complete == False:
        select = input("1: Meters and Feet, 2: Stones and Kilograms\n")
        try:
            select = int(select)
            if not select == 1 and not select == 2:
                raise Exception()
        except:
            print("Please enter a valid number, ensuring it is the value 1 or 2")
        else:
            select = int(select)
            complete = True
    if select == 1:
        print(metersFeet())
    if select == 2:
        print(stoneKilogram())

def convUtil(input1,way):
    if way == "mf":
        return(input1*3.281)
    if way == "fm":
        return(input1/3.281)
    if way == "sk":
        return(input1*6.35)
    if way == "ks":
        return(input1/6.35)


def metersFeet():
    complete3 = False
    while complete3 == False:
        select = input("1: Feet to Meters, 2: Meters to Feet\n")
        try:
            select = int(select)
            if not select == 1 and not select == 2:
                raise Exception()
        except:
            print("Please enter a valid number, ensuring it is the value 1 or 2")
        else:
            select = int(select)
            complete3 = True
    complete4 = False
    while complete4 == False:
        if select == 1:
            value1 = input("Input feet value: ") 
            try:
                value1 = float(value1)
            except:
                print("Enter a number.")
            else:
                value1 = float(value1)
                return(convUtil(value1,"fm"))
        if select == 2:
            value1 = input("Input meters value: ") 
            try:
                value1 = float(value1)
            except:
                print("Enter a number! Please!")
            else:
                value1 = float(value1)
                return(convUtil(value1,"mf"))

def stoneKilogram():
    complete3 = False
    while complete3 == False:
        select = input("1: Kilogram to Stone, 2: Stone to Kilogram\n")
        try:
            select = int(select)
            if not select == 1 and not select == 2:
                raise Exception()
        except:
            print("Please enter a valid number, ensuring it is the value 1 or 2")
        else:
            select = int(select)
            complete3 = True
    complete4 = False
    while complete4 == False:
        if select == 1:
            value1 = input("Input kilogram value: ") 
            try:
                value1 = float(value1)
            except:
                print("Enter a number.")
            else:
                value1 = float(value1)
                return(convUtil(value1,"ks"))
        if select == 2:
            value1 = input("Input stone value: ") 
            try:
                value1 = float(value1)
            except:
                print("Enter a number! Please!")
            else:
                value1 = float(value1)
                return(convUtil(value1,"sk"))


main()
