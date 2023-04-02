string = input("Digite uma palavra ou frase: ")
lista_caracteres = list(string)
tamanho_lista = len(lista_caracteres)

for i in range(tamanho_lista//2):
    temp = lista_caracteres[i]
    lista_caracteres[i] = lista_caracteres[tamanho_lista-i-1]
    lista_caracteres[tamanho_lista-i-1] = temp

string_invertida = "".join(lista_caracteres)

print(string_invertida)
