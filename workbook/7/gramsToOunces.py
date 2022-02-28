def GramsToOunces():
    Input = input("Enter grams: ")
    G = int(Input)
    if G <= 0:
        print("Invalid input.")
        Input = input("Enter grams:")
    Oz = G * 0.035274
    print("{}g = {}Oz".format(G, Oz))

GramsToOunces()
