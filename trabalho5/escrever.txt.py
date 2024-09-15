with open('texto.txt', 'w') as file:
    texto = list()
    texto.append("Esta é a primeira frase.")
    texto.append("Aqui está a segunda frase.")
    texto.append("E esta é a terceira frase.")

    for frase in texto:
        file.write(frase + '\n')

print("Frases foram escritas no arquivo texto.txt com sucesso. xD")
