# Napiste funkci digit_sum(n), ktera vrati ciferny soucet cisla n.


def digit_sum(num: int) -> int:
    n = num
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum

print(digit_sum(0))              # 0
print(digit_sum(274))            # 13
print(digit_sum(123456789))      # 45
print()



# Napiste funkci repeated_digit_sum(n), ktera opakovane vypocita ciferny
# soucet cisla n. Ze ziskaneho ciferneho souctu opet vypocita ciferny soucet
# (pokud se jedna o viceciferny soucet) a tento postup opakuje dokud nezbude
# jednociferne cislo, ktere vrati. Ke svemu reseni vyuzijte predchozi funkci.


def repeated_digit_sum(num: int) -> int:
    n = num
    while n >= 10:
        n = digit_sum(n)
    return n

print(repeated_digit_sum(123))               # 6
print(repeated_digit_sum(123456789))         # 9
print(repeated_digit_sum(99989788879879))    # 7
print()




# Pomoci textove grafiky vykreslete vyplneny ctverec o strane 5

#####
#####
#####
#####
#####


def print_full_square(size: int) -> None:
    for x in range(size):
        print("#" * size)

print_full_square(5)
print()




# Pomoci textove grafiky vykreslete prazdny ctverec o strane 5

#####
#   #
#   #
#   #
#####


def print_empty_square(size: int) -> None:
    print("#" * size)
    for i in range(size - 2):
        print("#", "#", sep = " " * (size - 2))
    print("#" * size)

print_empty_square(5)
print()


# Pomoci textove grafiky vykreslete sachovnici o velikosti 8x8

# # # #
 # # # #
# # # # 
 # # # #
# # # #
 # # # #
# # # #
 # # # #
 
def chessboard(size: int) -> None:
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print("#", end = "")
            else:
                print(" ", end = "")
        print()

chessboard(8)
print()


# Vypiste soucet prvnich N cisel pocinaje jednickou (pro jednicku vraci 1,
# pro dvojku 3, pro trojku 6, pro ctyrku 10, ...)

"""
1 -> 1
2 -> 1 + 2 -> 3
3 -> 1 + 2 + 3 -> 6
...
"""


def sum_first_n(num: int) -> int:
    n = num
    plus = 0
    while n > 0:
        plus += n
        n -= 1
    return plus

print(sum_first_n(4))


# BONUS


# Implementujte funkci, ktera prevede cislo z desitkove soustavy do binarni.
# Napriklad 21 je prevedeno na 10101.

def from_dec_to_bin(num: int) -> int:
    return 0  # TODO


# Implementujte funkci vracejici k-ty prvek fibonacciho rady. Fibonacciho
# rada zacina hodnotami 0, 1 a kazda dalsi hodnota je souctem dvou
# predchozich hodnot. Rada tedy pokracuje hodnotami 1, 2, 3, 5, 8, ...
# Na vstupu muzete ocekavat cela cisla vetsi nez nula.


def fibonacci(position: int) -> int:    
    return 0  # TODO


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_divisors_in = (1, 2, 3, 4, 111, 1000)
ib113_divisors_out = (1, 3, 6, 10, 6216, 500500)


def ib113_test_sum_first_n():
    print("Testovani funkce sum_first_n: ", end="")
    failure = False

    for i in range(len(ib113_divisors_in)):
        res = sum_first_n(ib113_divisors_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_divisors_out[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek"
                  .format(ib113_divisors_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_divisors_out[i]))
            break

    if not failure:
        print("OK")


ib113_from_dec_to_bin_entries = (0, 1, 2, 3, 7, 8, 9, 16, 21, 1024, 2047)
ib113_from_dec_to_bin_results = (0, 1, 10, 11, 111, 1000, 1001, 10000, 10101,
                                 10000000000, 11111111111)


def ib113_test_from_dec_to_bin() -> None:
    """Test funkce from_dec_to_bin."""
    print("\nTestovani funkce from_dec_to_bin: ", end="")
    failure = False

    for i in range(len(ib113_from_dec_to_bin_entries)):
        res = from_dec_to_bin(ib113_from_dec_to_bin_entries[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, ale typu {}".
                  format(type(res)))
            break
        if res != ib113_from_dec_to_bin_results[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek"
                  .format(ib113_from_dec_to_bin_entries[i]))
            print("Byla vracena hodnota: \"{}\"".format(res))
            print("Byla ocekavana hodnota: \"{}\"".
                  format(ib113_from_dec_to_bin_results[i]))
            break

    if not failure:
        print("OK")


ib113_fibonacci_entries = (1, 2, 3, 4, 5, 6, 7, 8, 15, 25)
ib113_fibonacci_results = (0, 1, 1, 2, 3, 5, 8, 13, 377, 46368)


def ib113_test_fibonacci() -> None:
    """Test funkce fibonacci."""
    print("\nTestovani funkce fibonacci: ", end="")
    failure = False

    for i in range(len(ib113_fibonacci_entries)):
        res = fibonacci(ib113_fibonacci_entries[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, ale typu {}".
                  format(type(res)))
            break
        if res != ib113_fibonacci_results[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek".
                  format(ib113_fibonacci_entries[i]))
            print("Byl navracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".
                  format(ib113_fibonacci_results[i]))
            break

    if not failure:
        print("OK")


# Zde muzete vkladat vlastni testy
if __name__ == '__main__':
    ib113_test_sum_first_n()
    ib113_test_from_dec_to_bin()
    ib113_test_fibonacci()



