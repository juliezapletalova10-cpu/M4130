print('Hello')
print('Brunko je goat')

print()

#rozlišuje O, sudé a liché čísla
x=0
if x==0:
    print('0')
elif x%2==0:
    print('sude')
else:
    print('liche')

print()

#vypiš čísla 1-50
for x in range (50):
    print(x+1, end=' ')

print()

x=0
while x<50:
    x+=1
    print(x, end=' ')

print()

#vypiš čísla od 1 do 50, které jsou dělitelné 5
x=0
while x<50:
    x+=1
    if x%5==0:
        print(x, end=' ')

print ()

x=0
for x in range(50):
    x+=1
    if x%5==0:
        print (x, end=' ')

print()

#(začátek, konec, krok)
for i in range (5,51,5):
    print(i, end=' ')
