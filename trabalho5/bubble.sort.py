def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array_numeros = [23, 4, 15, 8, 5, 11, 7, 35, 89, 50, 13, 27, 21, 66, 31]

bubbleSort(array_numeros)

print("Array ordenado:")
print(array_numeros)
