import os
ruta="test.txt"
#Bytes
size= os.path.getsize(ruta)

kb=size/1024
mb=size/(1024**2)

print(f"El tamaño del archivo es: {kb:.2f} KB")
print(f"El tamaño del archivo es: {mb:.4f} MB")
