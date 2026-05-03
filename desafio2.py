import numpy as np
from numpy import random as rd

# Gera 50.000 números inteiros aleatórios entre 0 e 100.000
numeros = np.random.randint(0, 100000, size=50000)


# ── Selection Sort ─────────────────────────────────────────────────────────────
def selection_sort(vetor):
    vetor = vetor.copy()
    n = len(vetor)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
    return vetor


# ── Insertion Sort ─────────────────────────────────────────────────────────────
def insertion_sort(vetor):
    vetor = vetor.copy()
    n = len(vetor)
    for i in range(1, n):
        elemento = vetor[i]
        j = i - 1
        while j >= 0 and elemento < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = elemento
    return vetor


# ── Shell Sort ─────────────────────────────────────────────────────────────────
def shell_sort(vetor):
    vetor = vetor.copy()
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


# ── Merge Sort ─────────────────────────────────────────────────────────────────
def merge_sort(vetor):
    if len(vetor) <= 1:          # condição de parada corrigida
        return vetor
    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita  = merge_sort(vetor[meio:])
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