import numpy as np
from numpy import random as rd

# Gera 50.000 números inteiros aleatórios entre 0 e 100.000
# np.random.randint(low, high, size) → valores no intervalo [low, high)
numeros = np.random.randint(0, 100000, size=50000)


# ── Selection Sort ─────────────────────────────────────────────────────────────
# Complexidade: O(n²) no melhor, médio e pior caso
# Estratégia: a cada iteração, encontra o menor elemento do trecho não ordenado
# e o coloca na posição correta (início do trecho).
def selection_sort(vetor):
    vetor = vetor.copy()          # evita modificar o array original
    n = len(vetor)
    for i in range(n):            # i = limite da parte já ordenada
        min_idx = i               # assume que o mínimo está na posição atual
        for j in range(i + 1, n):             # varre o restante do vetor
            if vetor[j] < vetor[min_idx]:     # encontrou um valor menor
                min_idx = j                   # atualiza o índice do mínimo
        # troca o mínimo encontrado com a posição i (desempacotamento Python)
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
    return vetor


# ── Insertion Sort ─────────────────────────────────────────────────────────────
# Complexidade: O(n) melhor caso (já ordenado) | O(n²) médio e pior caso
# Estratégia: funciona como ordenar cartas na mão — pega um elemento e o
# insere na posição correta dentro da parte já ordenada (à sua esquerda).
def insertion_sort(vetor):
    vetor = vetor.copy()          # evita modificar o array original
    n = len(vetor)
    for i in range(1, n):         # começa no índice 1; índice 0 já é "ordenado"
        elemento = vetor[i]       # elemento a ser inserido na posição correta
        j = i - 1                 # começa a comparar com o vizinho à esquerda
        # desloca elementos maiores uma posição para a direita
        while j >= 0 and elemento < vetor[j]:
            vetor[j + 1] = vetor[j]   # empurra o elemento uma posição à direita
            j -= 1                     # move o ponteiro para a esquerda
        vetor[j + 1] = elemento        # insere o elemento na lacuna criada
    return vetor


# ── Shell Sort ─────────────────────────────────────────────────────────────────
# Complexidade: depende da sequência de intervalos; aqui (n/2, n/4, …) → O(n²)
# pior caso, mas na prática bem mais rápido que Insertion Sort puro.
# Estratégia: generalização do Insertion Sort — ordena elementos distantes
# entre si (gap = intervalo), reduzindo o gap pela metade a cada rodada até
# gap = 1, quando se torna um Insertion Sort sobre um vetor quase ordenado.
def shell_sort(vetor):
    vetor = vetor.copy()          # evita modificar o array original
    n = len(vetor)
    intervalo = n // 2            # gap inicial = metade do tamanho do vetor
    while intervalo > 0:
        # Insertion Sort com passo = intervalo (em vez de passo 1)
        for i in range(intervalo, n):
            temp = vetor[i]       # elemento que será reposicionado
            j = i
            # desloca elementos distantes `intervalo` posições enquanto maior
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]   # move elemento para frente
                j -= intervalo                     # recua um "passo"
            vetor[j] = temp       # insere temp na posição correta
        intervalo //= 2           # reduz o gap pela metade a cada passagem
    return vetor


# ── Merge Sort ─────────────────────────────────────────────────────────────────
# Complexidade: O(n log n) em todos os casos
# Estratégia: divisão e conquista — divide o vetor ao meio recursivamente até
# restar subarrays de 1 elemento (já "ordenados"), depois mescla os pares de
# subarrays em ordem crescente, subindo até reconstituir o vetor completo.
def merge_sort(vetor):
    # Caso base: vetor de 0 ou 1 elemento já está ordenado por definição
    if len(vetor) <= 1:
        return vetor
    meio = len(vetor) // 2               # índice do ponto de divisão
    esquerda = merge_sort(vetor[:meio])  # ordena recursivamente a metade esquerda
    direita  = merge_sort(vetor[meio:])  # ordena recursivamente a metade direita
    return mesclar(esquerda, direita)    # combina as duas metades ordenadas

def mesclar(esquerda, direita):
    """
    Intercala dois subarrays ordenados em um único array ordenado.
    Compara os primeiros elementos de cada subarray e move o menor
    para o resultado, repetindo até esgotar um dos lados; o restante
    do outro lado é concatenado diretamente (já está ordenado).
    """
    ordenado = []
    e = esquerda.tolist()   # converte para lista Python para usar pop(0)
    d = direita.tolist()
    # enquanto ambos os lados tiverem elementos, compara os primeiros
    while e and d:
        if e[0] <= d[0]:
            ordenado.append(e.pop(0))   # menor vem da esquerda
        else:
            ordenado.append(d.pop(0))   # menor vem da direita
    # um dos lados pode ainda ter elementos — concatena sem comparação
    return np.array(ordenado + e + d)