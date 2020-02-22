
from io import open

archivo_texto=open("archivo.txt","r+") #lectura y escritura

lista_texto=archivo_texto.readlines();

lista_texto[1]="incluir esto \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

a= "paja"

print(a.lower().uppercase()) 



