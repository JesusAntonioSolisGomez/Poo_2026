###
## excepciones basicas

#parte 1 try/ except simple

print("="*50)
print("Parte 1: Division con manejo de errores")
print("="*50)

try:
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))  
    total = a / b
    
except ValueError:
    print("Error: SOLO NUMEROS, no otros caracteres.")
    
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
    
else:
    print(f"El resultado de {a} / {b} es: {total}") 
    
finally:
    print("Fin del programa.")  
    


