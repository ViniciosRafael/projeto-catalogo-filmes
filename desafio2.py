import numpy as np
from numpy import random as rd
import timeit

numeros = rd.randint(0, 100000, size=1000)
#gera o vetor uma única vez para garantir que todos os algoritmos ordenem o mesmo conjunto de dados

# Big-O:
#   Melhor caso:  O(n²)
#   Pior caso:    O(n²)

def selection_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        min_idx = i # assume que o mínimo do trecho está na posição i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[min_idx]:
                min_idx = j # atualiza o índice do mínimo encontrado
        if min_idx != i:
            trocas += 1 # só conta troca se o mínimo não estava já no lugar
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
    return vetor, comparacoes, trocas

# Big-O:
#   Melhor caso:  O(n)   — vetor já ordenado; o while interno nunca executa
#   Pior caso:    O(n²)  — vetor em ordem inversa

def insertion_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    comparacoes = 0
    trocas = 0
    for i in range(1, n):
        elemento = vetor[i] # elemento a ser inserido na posição correta
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if elemento < vetor[j]:
                vetor[j + 1] = vetor[j] # desloca elemento maior para a direita
                trocas += 1
                j -= 1
            else:
                break # posição correta encontrada
        vetor[j + 1] = elemento # insere o elemento na posição correta
    return vetor, comparacoes, trocas

# Big-O:
#   Melhor caso:  O(n log n) — com sequência de intervalos otimizada
#   Pior caso:    O(n²)

def shell_sort(numeros):
    vetor = numeros.copy()
    n = len(vetor)
    intervalo = n // 2 # gap inicial: metade do tamanho do vetor
    comparacoes = 0
    trocas = 0
    while intervalo > 0:
        # Aplica Insertion Sort com o gap atual em todas as sub-listas
        for i in range(intervalo, n):
            temp = vetor[i]
            j = i
            while j >= intervalo:
                comparacoes += 1
                if vetor[j - intervalo] > temp:
                    vetor[j] = vetor[j - intervalo] # desloca elemento
                    trocas += 1
                    j -= intervalo
                else:
                    break
            vetor[j] = temp # insere o elemento na posição correta do sub-array
        intervalo //= 2 # reduz o gap pela metade
    return vetor, comparacoes, trocas

#   Big-O:
#   Melhor caso:  O(n log n)
#   Pior caso:    O(n log n)

def merge_sort(numeros):
    comparacoes = [0]
    trocas = [0]

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr # caso base: array com 0 ou 1 elemento já está ordenado
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
                ordenado.append(e.pop(0)) # elemento da esquerda é menor
            else:
                ordenado.append(d.pop(0)) # elemento da direita é menor
                trocas[0] += 1
        return np.array(ordenado + e + d)

    resultado = _merge_sort(numeros) # concatena sobras
    return resultado, comparacoes[0], trocas[0]


def formatar_tempo(segundos): # Converte um valor em segundos (float) para o formato HH:MM:SS:mmm.
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs = int(segundos % 60)
    milissegundos = int((segundos % 1) * 1000)
    return f"{horas:02}:{minutos:02}:{segs:02}:{milissegundos:03}"


def exibir(nome, func, numeros): #  Executa e exibe as métricas de um algoritmo de ordenação
    _, comparacoes, trocas = func(numeros)
    tempo = timeit.timeit(lambda: func(numeros), number=1)
    print(f"{nome}:")
    print(f"  Tempo:       {tempo:.6f}s e {formatar_tempo(tempo)}")
    print(f"  Comparações: {comparacoes}")
    print(f"  Trocas:      {trocas}")
    print()


print("Tamanho do vetor:", len(numeros))
print()
exibir("Selection Sort", selection_sort, numeros)
exibir("Insertion Sort", insertion_sort, numeros)
exibir("Shell Sort",     shell_sort,     numeros)
exibir("Merge Sort",     merge_sort,     numeros)