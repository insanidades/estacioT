from random import randint

array = [randint(1, 100) for x in range(15)]
print("Array não ordenado:")
print(array)

for i in range(len(array)):
    receba = i

    for j in range(i + 1, len(array)):
        if array[j] < array[receba]:
            receba = j

    array[i], array[receba] = array[receba], array[i]

print("\nArray ordenado:")
print(array)
