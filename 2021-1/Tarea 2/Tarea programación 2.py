
#Datos de nevarro nurmies
    #Nevarro_nummies_grasas= 1.90
    #Nearro_nummies_carbohidratos= 6.00
    #Nevarro_nummies_proteínas= 0.80

#Datos de space soup
    #Space_soup_grasas= 10.0
    #Space_soup_carbohidratos= 12.0
    #Space_soup_proteínas= 11.0

#Datos de carne de rana
    #Carne_de_rana_grasas= 0.30
    #Carne_de_rana_carbohidratos= 0.00
    #Carne_de_rana_proteínas= 16.0

#Datos de calorias
    #1[g]grasa = 9
    #1[g]Carbohidrato=4
    #1[g]Proteína=4


#Datos a solicitar
Nevarro_nummies= float(input(" Nevarro Nummies consumidas (en unidades): "))
Space_soup= float(input(" Space Soup consumida (en [ml]): "))
Carne_de_rana= float(input("Carne de rana consumida (en [g]): "))


#Cálculo de grasas, carbohidratos y proteínas por alimento
#nevarro nummies
Nevarro_n_grasas= 1.90*Nevarro_nummies
Nevarro_n_carbohidratos= 6.00*Nevarro_nummies
Nevarro_n_proteínas= 0.80*Nevarro_nummies

#space soup
Space_s_grasas= (10.0/285)*Space_soup
Space_s_carbohiratos= (12.0/285)*Space_soup
Space_s_proteínas= (11.0/285)*Space_soup

#carne de rana
Carne_r_grasas=(0.30/100)*Carne_de_rana
Carne_r_carbohiratos=(0.00/100)*Carne_de_rana
Carne_r_proteínas=(16.0/100)*Carne_de_rana


#Cálculo de grasas, carbohidratos y proteínas en total
Grasas= (Nevarro_n_grasas + Space_s_grasas + Carne_r_grasas)
Carbohidratos= (Nevarro_n_carbohidratos + Space_s_carbohiratos + Carne_r_carbohiratos)
Proteínas= (Nevarro_n_proteínas + Space_s_proteínas + Carne_r_proteínas)

#Calculo calorias
Calorias_grasas= Grasas*9 
Calorias_carbohidratos= Carbohidratos*4 
Calorías_proteínas= Proteínas*4

#Muestra de resultadoa
print ("Grogu ha consumido:")
print ((round(Grasas,2), "[g] de grasas"))
print ((round(Carbohidratos,2), "[g] de carbohidratos"))
print ((round(Proteínas,2), "[g] de proteínas"))
print ("dando un total de")
print ((round(Calorias_grasas + Calorias_carbohidratos + Calorías_proteínas,2),"[calorias]"))



#Casos de prueba
#Caso1
        #Nevarro Nummies consumidas (en unidades): 4
        #Space Soup consumida (en [ml]): 300
        #Carne de rana consumida (en [g]): 320.5
        #Grogu ha consumido:
        #19.09 [g] de grasas
        #36.63 [g] de carbohidratos
        #66.06 [g] de proteinas
        #dando un total de
        #582.55 [calorias]

#Caso2
        #Nevarro Nummies consumidas (en unidades): 7
        #Space Soup consumida (en [ml]): 550.5
        #Carne de rana consumida (en [g]): 470
        #Grogu ha consumido:
        #34.03 [g] de grasas
        #65.18 [g] de carbohidratos
        #102.05 [g] de proteinas
        #dando un total de
        #975.14 [calorias]

#Caso3
        #Nevarro Nummies consumidas (en unidades): 2.5
        #Space Soup consumida (en [ml]): 120
        #Carne de rana consumida (en [g]): 225
        #Grogu ha consumido:
        #9.64 [g] de grasas
        #20.05 [g] de carbohidratos
        #42.63 [g] de proteinas
        #dando un total de
        #337.46 [calorias]


#comentario general
#Lo primero que hara el programa será recibir los datos solicitados
#Una vez el programa tenga estos datos, calculará las grasas, los carbohidratos y proteinas de cada tipo de comida (por orden de variables), realizando la conversión de unidades correspondiente 
#Luego sumara las grasas de los 3 tipos de comida, luego de los carbohidratos y despues de las proteinas (se podría decir como una suma de terminos comunes)
#Finalmente calculara la cant. de calorias de grasas, carbohidratos y proteinas, para esto multiplica el valor del total de las anteriores mencionadas por su equivalente en calorías 
#Ya con estos datos listos imprime los resultados de grasas, carbohidratos y proteínas, redondeando a su 2do decimal. Y con las calorías, lo que hace es sumarlas y redondear el valor a 2 decimales y esto lo imprime










