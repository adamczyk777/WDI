def informacjeUklad(x, y):
    if x == 0:
        print ("Punkt znajduje się na osi y")
    elif y == 0:
        print ("Punkt znajduje się na osi x")
    elif y >0 and x > 0:
        print ("punkt znajduje się w pierwszej ćwiartce")
    elif y> 0 and x < 0:
        print ("punkt znajduje się w drugiej ćwiartce")
    elif x < 0 and y < 0 :
        print ("punkt znajduje się w trzeciej ćwiartce")
    elif y < 0 and x > 0:
        print ("punkt znajduje się w czwartej ćwiartce")

wspX = int(input("Podaj wsporrzrdna x: "))
wspY = int(input("Podaj wspolrzedna y: "))

informacjeUklad(wspX, wspY)
