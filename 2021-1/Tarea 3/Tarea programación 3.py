#datos solicitados,el programa funcionara segun las condiciones otorgadas, si algo no esta dentro de la condición se imprimira "error"
Valor_propiedad= int(input("Valor propiedad en UF (1500-13000): "))
if Valor_propiedad >=1500 and Valor_propiedad <= 13000:
    Pie= int(input("Ingrese % del Pie (20%-45%): "))
    if Pie >=20 and Pie <=45:
        Plazo= int(input(" Ingrese plazo (20,25,30): "))
        if Plazo == 20 or Plazo== 25 or Plazo== 30:
            Tipo_vivienda= int(input("Tipo vivienda Casa(1) o Departamento (2): "))
            if Tipo_vivienda == 1 or Tipo_vivienda == 2:
                Estado_de_vivienda= int(input("Estado vivienda Nueva (1) o Usada (2) "))
                if Estado_de_vivienda == 1 or Estado_de_vivienda==2:
                    #se calcula el total de la vivienda menos el valor del pie
                    monto_casa_con_pie= Valor_propiedad-(Valor_propiedad*(Pie/100))
                    if Tipo_vivienda==1 and Estado_de_vivienda==1:
                        seguros_en_uf_mensuales=(0.5+0.8)
                        if Plazo ==20:
                            interes= 25/100 
                            #calculo de intereses de la vivienda
                            intereses_uf= monto_casa_con_pie*interes
                            #suma interes y total de la vivienda (a la vivienda ya se le descontó el valor del pie)
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            #calculo del total del seguro 
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            #calculos de credito y dividendo de el valor definitivo de la casa (es decir, con sus seguros correspondientes incluidos)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            #impresión valores redondeandolos a 2 decimales
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
#Para calcular los montos de cada caso, se siguen los mismos pasos realizados en el caso 1
                        elif Plazo==25:
                            interes=30/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                        elif Plazo==30:
                            interes= 35/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                    if Tipo_vivienda==1 and Estado_de_vivienda==2:
                        seguros_en_uf_mensuales=0.5
                        if Plazo==20:
                            interes= 22/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                        elif Plazo ==25:
                            interes= 27/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            seguros_en_uf_mensuales= (0.5)
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                        elif Plazo==30: 
                            interes= 31/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            seguros_en_uf_mensuales= (0.5)
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")        
                    if Tipo_vivienda==2 and Estado_de_vivienda==1:
                        seguros_en_uf_mensuales= (0.5+0.8+0.3)
                        if Plazo ==20:
                            interes= 28/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                        elif Plazo ==25:
                            interes= 33/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                        elif Plazo ==30:
                            interes= 41/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")       
                    if Tipo_vivienda==2 and Estado_de_vivienda==2:
                        seguros_en_uf_mensuales =(0.5+0.3)
                        if Plazo ==20:
                            interes= 26/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ",round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2) , "UF")
                        elif Plazo ==25:
                            interes= 32/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                        elif Plazo ==30:
                            interes= 37/100
                            intereses_uf= monto_casa_con_pie*interes
                            vivienda_sin_seguros=monto_casa_con_pie+intereses_uf
                            total_seguro=seguros_en_uf_mensuales*(Plazo*12)
                            total_credito_pagar= vivienda_sin_seguros+total_seguro
                            dividendo= total_credito_pagar/(Plazo*12)
                            print ("Total del credito a pagar: ", round (total_credito_pagar,2), "UF")
                            print ("dividendo mensual de: ", round (dividendo,2), "UF")
                    
                    
                else:
                    print ("Estado de vivienda inválido")
            else:
                print ("Tipo de vivienda inválido")        
        else:
            print ("Plazo inválido") 
    else:
        print ("Error: Pie fuera de rango")
else:
    print ("Error: Valor fuera de rango")


    





