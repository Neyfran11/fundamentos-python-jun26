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



#player1 = "Messi"

#player2 = "Ronaldo"

#sel_player1 = "piedra"
#sel_player2 = "tijeras"

#if sel_player1 == "piedra":
   # print(f"{player1} piedra para tijeras")
   # print(f"{player1} tijeras para papel")
  #  print(f"{player1} papel para piedra")

#elif sel_player2 == "Ronaldo":
    #print(f"{player2} piedra para tijeras")
   # print(f"{player2} tijeras para papel")
   # print(f"{player2} papel para piedra")



# Estrcuturas de datos
name_list = ["Alfredo", "Primero", "Segundo", "Tercero"]
age_list = [18, 20, 30, 40]
weights_list = [50.5, 60.5, 70.5, 80.5]

name_list2 = [
              "Alfredo"
              "Primero"
              "Segundo"
              "Tercero"
]


# agregando elementos a la lista
#name_list.append("Cuarto")

#print(len(name_list))

#print(name_list)

#print(name_list[2]) # Segundo
#print(name_list[0]) # Alfredo
#print(name_list[1]) # Primero
#print(name_list[3]) # Tercero

# mostrar un slice de la lista 
#print(name_list[1:3]) # ['Alfredo', 'Primero']

#el ultimo elemento de la lista
#print(name_list[-1]) # Tercero

# cambiar el valor del primer elemento de la lista
#name_list[0] = "ruperto" 
#print(name_list) # ['ruperto', 'Primero', 'Segundo', 'Tercero']

# tuplas
#name_tuple = (
  #  "Alfredo", 
   # "Primero", 
    #"Segundo", 
    #"Tercero")

#print(name_tuple[0]) # Alfredo

# diccionario 

name_dict = {
    "name": "Alfredo",
    "last_name": "Primero",
    "age": 20,
    "weight": 70.5,
    "favorite_foods": ["Pizza", "Hamburguesa", "Tacos"],
    "address": {
        "zip_code": "12345",
        "street": "Calle 123",
        "city": "lecheria",
        "country": "Pais",
    }
}

#print(name_dict["address"]["city"]) # ciudad
#print(name_dict["favorite_foods"][1]) # Hamburguesa

# bucles
#for name in name_list:
 #   if name == "Segundo":
 #       print(f"hola {name}")

len(name_list)
for var in range(len(name_list)):
    print(f"Hola {name_list[var]}")

