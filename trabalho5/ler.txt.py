arquivo = open('loremipsum.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print("Conteúdo completo:")
print(conteudo)

arquivo = open('loremipsum.txt', 'r')
primeira_linha = arquivo.readline().strip()
arquivo.close()

print("\nPrimeira linha do arquivo:")
print(primeira_linha)

print("\nPrimeiros 3 caracteres do arquivo:")
print(conteudo[:3])

with open('loremipsum.txt', 'r') as arquivo:
    conteudo_with = arquivo.read()

print("\nConteúdo do arquivo lido com 'with':")
print(conteudo_with)
