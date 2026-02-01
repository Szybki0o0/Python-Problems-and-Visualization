import random

# jak działa enumerate()
supplies = ['japko','kalafior','śliwka','banan']
print(supplies)
for index, item in enumerate(supplies):
    print(str(index), item, supplies[index])

# jak działa random.choise() i random.shuffle()
print(random.choice(supplies))
random.shuffle(supplies)
print(supplies)

# metody list
print(supplies.index('japko'))
supplies.append('gruszka')
supplies.insert(2,'brokuł')
print(supplies)
supplies.remove('kalafior')
supplies.sort()
print(supplies)
supplies.reverse()
print(supplies)

# listy mogą być modyfokowane jednak ciągi tekstowe i kortki (tuple) nie mogą
# można zmieniać listy i krotki i ciągi tekstowe za pomocą funkcji list() i tuple()

# Odwołania
bibeloty = supplies
bibeloty[1] = 2
print(supplies)

# Przypisując jedną listę do drugiej tworzy się odwołanie a nie przypisanie
# nie jest tak ze zmiennymi

# Funkzja id() zwraca adres zmiennej
print(id(bibeloty))
print(id(supplies))