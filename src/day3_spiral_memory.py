#!/usr/bin/env python3
import sys


def first(address):
    # calcolo in che livello è finito il mio elemento
    level = 0
    side_size = 0
    base_addr = 0

    for level in range(0, sys.maxsize):
        side_size = 2 * level + 1
        base_addr = side_size ** 2
        if base_addr >= address:
            break

    # trovo il centro del lato
    while base_addr > address:
        base_addr -= side_size - 1
    base_addr += (side_size - 1) / 2

    return abs(address - base_addr) + level


def second(threshold):
    # cache dei livelli già calcolati
    cache = {0: [1]}

    def isangle(l_size, p):
        return (p + 1) % (l_size / 4) == 0

    level = 0
    position = 0
    while True:
        # avanzo di 1
        position += 1

        # in ogni livello ci stanno esattamente x elementi dove:
        # x = (2n+1)**2 - (2*(n-1)+1)**2
        #   = 4n**2 + 4n + 1 - (4(n-1)**2 + 4(n-1) + 1)
        #   = 4(n**2 + n - (n-1)**2 - (n-1))
        #   = 8n
        level_size = 8 * level

        # controllo se passo al prossimo livello
        if position >= level_size:
            level += 1
            position = 0
            level_size = 8 * level

        if level in cache:
            current_level = cache[level]
        else:
            current_level = []
            cache[level] = current_level
        previous_level = cache[level - 1]

        # ogni numero è dato da:
        # livello 0: 1 (calcolato prima di entrare nel loop

        # calcolo l'indice dell'elemento sottostante
        if level == 1:
            under = 0
        elif position == 0:
            under = 0
        else:
            # tolgo 1 perché comincio più in basso di 1
            under = position - 1
            # ogni livello ha 2 elementi in più per lato
            under -= 2 * (position // (level_size // 4))
            # ma gli angoli usano lo stesso valore dell'elemento precedente
            if isangle(level_size, position):
                under -= 1

        # questo ce l'ho sempre
        current = previous_level[under]
        # i primi 2 vedono l'ultimo del livello precedente
        if level > 1 and position <= 1:
            current += previous_level[-1]
        if position > 0:
            # prendo il numero precedente a parte per il primo del livello
            current += current_level[position - 1]
            # gli ultimi 2 del livello vedono anche il primo del livello
            if position >= level_size - 2:
                current += current_level[0]
            # nelle posizioni dopo gli angoli vedo anche 2 numeri prima
            if isangle(level_size, position - 1):
                current += current_level[position - 2]
            if not isangle(level_size, position):
                # prendiamo i numeri del livello sotto tranne negli angoli e dopo gli angoli
                if not isangle(level_size, position - 1) and under > 0:
                    current += previous_level[under - 1]
                # questo c'è tranne nel primo e gli ultimi 2 del livello e prima degli angoli
                if not isangle(level_size, position + 1) and under + 1 < len(previous_level):
                    current += previous_level[under + 1]

        if current > threshold:
            return current

        # salvo in cache
        current_level.append(current)


if __name__ == '__main__':
    # res = first(1)
    # print(">>> %d" % res)
    #
    # res = first(12)
    # print(">>> %d" % res)
    #
    # res = first(23)
    # print(">>> %d" % res)
    #
    # res = first(1024)
    # print(">>> %d" % res)
    #
    # res = first(325489)
    # print(">>> %d" % res)

    res = second(325489)
    print(">>> %d" % res)
