print("Escriu una distància en centímetres")
centímetres = input()
a = int(centímetres)%100
b = int(centímetres)%100000
km = (int(centímetres) - b)/100000
m = (int(centímetres) - a)/100

if ( int(centímetres) <= 0):
    print ("La distància ha de ser major a cero")

else:
        print (centímetres + " " + "centímetres són")

        if (int(centímetres) >= 100000):
            print (str(km) + " " + "kilómetres")
        else:
                print(str(0) + "kilómetres")

        if (int (centímetres) >=100):
            print (str(m) + " " + "metres")
        else:
            print (str(0)+ " " + "metres")

        if(int(centímetres) > 0):
            print("i" + " " + str(centímetres) + " " + "centímetres")














