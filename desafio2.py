import numpy as np
from numpy import random as rd
import timeit

numeros = rd.randint(0, 100000, size=1000)


def selection_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        if min_idx != i:
            trocas += 1
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
    return vetor, comparacoes, trocas


def insertion_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    comparacoes = 0
    trocas = 0
    for i in range(1, n):
        elemento = vetor[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if elemento < vetor[j]:
                vetor[j + 1] = vetor[j]
                trocas += 1
                j -= 1
            else:
                break
        vetor[j + 1] = elemento
    return vetor, comparacoes, trocas


def shell_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    intervalo = n // 2
    comparacoes = 0
    trocas = 0
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = vetor[i]
            j = i
            while j >= intervalo:
                comparacoes += 1
                if vetor[j - intervalo] > temp:
                    vetor[j] = vetor[j - intervalo]
                    trocas += 1
                    j -= intervalo
                else:
                    break
            vetor[j] = temp
        intervalo //= 2
    return vetor, comparacoes, trocas


def merge_sort(numeros):
    comparacoes = [0]
    trocas = [0]

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr
        meio = len(arr) // 2
        esquerda = _merge_sort(arr[:meio])
        direita = _merge_sort(arr[meio:])
        return _mesclar(esquerda, direita)

    def _mesclar(esquerda, direita):
        ordenado = []
        e = esquerda.tolist()
        d = direita.tolist()
        while e and d:
            comparacoes[0] += 1
            if e[0] <= d[0]:
                ordenado.append(e.pop(0))
            else:
                ordenado.append(d.pop(0))
                trocas[0] += 1
        return np.array(ordenado + e + d)

    resultado = _merge_sort(numeros)
    return resultado, comparacoes[0], trocas[0]


def exibir(nome, func, numeros):
    _, comparacoes, trocas = func(numeros)
    tempo = timeit.timeit(lambda: func(numeros), number=1)
    print(f"{nome}:")
    print(f"  Tempo:       {tempo:.6f}s")
    print(f"  Comparações: {comparacoes}")
    print(f"  Trocas:      {trocas}")
    print()


print("Tamanho do vetor:", len(numeros))
print()
exibir("Selection Sort", selection_sort, numeros)
exibir("Insertion Sort", insertion_sort, numeros)
exibir("Shell Sort",     shell_sort,     numeros)
exibir("Merge Sort",     merge_sort,     numeros)