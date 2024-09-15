from random import randint

array_inteiros = [randint(1, 100) for x in range(15)]
print("Conteúdo do array:")
print(array_inteiros)

array_inteiros.sort()
print("\nArray de inteiros ordenado em ordem crescente:")
print(array_inteiros)

array_inteiros.sort(reverse=True)
print("\nArray de inteiros ordenado em ordem decrescente:")
print(array_inteiros)

array_strings = ["nome", "dataNascimento", "cpf", "rg"]

array_strings.sort()
print("\nArray de strings ordenado em ordem crescente:")
print(array_strings)

array_strings.sort(reverse=True)
print("\nArray de strings ordenado em ordem decrescente:")
print(array_strings)
