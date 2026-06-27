# variables
name = "alfredo"

last_name = "primero"

Last_name = "segundo"

Last_Name = "tercero"

#ast.name = "primero"

print()

# operadores matematicos
num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2

#print(suma)
#print(resta)
#print(multi)
#print(div)

#print(f"el resultado de la suma es: {suma}")
#print(f"el resultado de la resta es: {resta}")
#print(f"el resultado de la multiplicacion es: {multi}") 
#print(f"el resultado de la division es: {div}")

#Operadores de comparacion
# Mayor que >
# Menor que <
# Mayor igual >=
# Menor igual <=
# igual ==
# diferente !=

#print(num1 > num2)
#print(num1 <= num2)
#print(num1 == num2)
#print(num1 != num2)

# condicionales
#if num1 > num2:
    #print(f"{num1} es mayor que {num2}")

#if num2 > num1:
#    print(f"{num1} es mayor que {num2}")
#else:
  #  print(f"{num1} es menor que {num1}")

# condicionales anidados

#edad = 18
#genero = "mujer"
#dia = ["jueves", "sabado"]

#if edad >= 18:
    #if genero == "mujer":
       # if dia == "jueves":
        #    print("Puedes pasar")
        #else:
       #     print("No puedes pasar,solo jueves")

       # print("Puedes pasar")
    #else:
       # print("No puedes pasar,solo mujeres")    
#else:
    #print("No puedes pasar,solo mujeres")

    #operadores logicos
    #if (edad > 18) and (genero == 'mujer') and (dia == 'jueves') or (dia == "sabado"):
      #  print("Puedes pasar")
    #else:
       # print("No puedes pasar")

       # condicionales endadenados, para identificar el fin de semana
       #if dia == "viernes":
          # print("Hoy es viernes Fin de semana")

        # elif dia == "sabado":
             #print("Hoy es sabado Fin de semana")

            ##elif dia == "domingo":
              #  print("Hoy es domingo Fin de semana")

#juego de piedra, papel o tijeras con condicionales



player1 = "Messi"

player2 = "Ronaldo"

sel_player1 = "piedra"
sel_player2 = "tijeras"

if sel_player1 == "piedra":
    print(f"{player1} piedra para tijeras")
    print(f"{player1} tijeras para papel")
    print(f"{player1} papel para piedra")

elif sel_player2 == "Ronaldo":
    print(f"{player2} piedra para tijeras")
    print(f"{player2} tijeras para papel")
    print(f"{player2} papel para piedra")

