#y prednasky, chceme tabulku a aby nam program udelal celkovy soucet
total = 0
for j in range(10):
    for i in range(10):
        print (i+j+1, end=" ")
        total += i+j+1
    print()
print("Total:", total)

print()

a = 1
b = 2 
print(a + b)

print()

a = "1"
b = "2"
print(a + b)

print()

#1c, 2b, 3e, 4f, 5a, 6g, 7d
#for i in range(n), jede pro i od 0 do n-1

#objem kvadru a koule
from math import pi
side_a = 2
side_b = 3
side_c = 4
volume_kvadru = side_a * side_b * side_c
print("Objem kvadru je roven", volume_kvadru, "cm^3")


r = 5
volume_koule = (4/3) * pi * r**3
print("Objem koule je roven", volume_koule, "cm^3")

print()

#vypiste prvnich 10 mocnin cisla 2
for i in range(10):
    x = 2**i
    print(x, end=" ")

print()

#vzpiste prvnich 15 prvku Fibonnaciho posloupnosti
x = 0
y = 1
for i in range(15):
    print(x, end=" ")
    z = x + y
    x = y
    y = z

print()

#vypiste prvky posloupnosti, jejichz prvni prvky vypadaji nasledovne a) 1 -1 2 -2 3 -3 .... b) 1 1 2 1 2 3 1 2 3 4 .....
for i in range (11):
    print(i, -i, end = " ")
    

print()

for i in range (1, 11):
    for j in range (1, i + 1):
        print(j, end = " ")

print()

#naleznete a vypiste vsechny delitele daneho cisla
#cislo zadejte pomoci promenne
#cisla vypiste na jeden radek oddelena carkou
#pro 0 a zaporna cisla vypiste chybovou hlasku

x = 24
if x <= 0:
    print("Chyba")
else:
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end = ", ")

print()

#prevedte predchozi priklady do funkci, ktere spustite

def power(base, repete):
    for i in range(repete):
        x = base ** i
        print (x, end = " ")
    print()

power(2, 10)

def fibonnaci(howmany):
    x = 0
    y = 1
    for i in range(howmany):
        print(x, end = " ")
        z = x + y
        x = y
        y = z
    print()

fibonnaci(15)

def limit1(endwith):
    for i in range(1, endwith + 1):
        print(i, -i, end = " ")
    print ()

limit1(10)

def limit2(length):
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
    print()

limit2(10)

def divisors(number):
    if number <= 0:
        print("Chyba")
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                print(i, end = ", ")
    print()

divisors(24)