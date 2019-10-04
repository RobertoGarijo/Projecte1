print ("Defineix la pendent")
pendent = input()

print ("Defineix el valor de x")
x = input()

print ("Defineix constant de la recta")
constant = input()

def equació_recta(pendent,x,constant):
    return pendent * x + constant
y = equació_recta(int(pendent),int(x),int(constant))
print ("El resultat de l'equació és  : " + str(y))

    
