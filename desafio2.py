import numpy as np
from numpy import random as rd
import timeit

numeros = rd.random.randint(0, 100000, size=1000)


def selection_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
    return vetor


def insertion_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    for i in range(1, n):
        elemento = vetor[i]
        j = i - 1
        while j >= 0 and elemento < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = elemento
    return vetor


def shell_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2
    return vetor


def merge_sort(numeros):
    if len(numeros) <= 1:
        return numeros
    meio = len(numeros) // 2
    esquerda = merge_sort(numeros[:meio])
    direita  = merge_sort(numeros[meio:])
    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    ordenado = []
    e = esquerda.tolist()
    d = direita.tolist()
    while e and d:
        if e[0] <= d[0]:
            ordenado.append(e.pop(0))
        else:
            ordenado.append(d.pop(0))
    return np.array(ordenado + e + d)

print ("Selection Sort:", selection_sort)
print (timeit.timeit('selection_sort(numeros)', globals=globals(), number=1), "segundos")
print ("Insertion Sort:", insertion_sort)
print (timeit.timeit('insertion_sort(numeros)', globals=globals(), number=1), "segundos")
print ("Shell Sort:", shell_sort)
print (timeit.timeit('shell_sort(numeros)', globals=globals(), number=1), "segundos")
print ("Merge Sort:", merge_sort)
print (timeit.timeit('merge_sort(numeros)', globals=globals(), number=1), "segundos")