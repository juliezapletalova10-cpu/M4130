# Napiste funkci, ktera vam vrati retezec s pismeny usporadanymi pozpatku.


#def reverse(text):
    #return text[::-1]

def reverse(text):
    result = ""
    for i in range(len(text)):
        result = text[i] + result
    return result

def reverse_char(text): 
    result = ""  
    for character in text:
        result = character + result
    return result

print(reverse("ONMEJATEJOLSEH"))
# HESLOJETAJEMNO
print(reverse_char("ONMEJATEJOLSEH"))
print()


# Mezi kazda dve pismena daneho textu vlozte dodany text (jako novy parametr
# funkce)

def reverse_for_dummies(text, rubbish):
    result = ""
    for i in range(len(text)):
        result += text[i]
        if i < len(text) - 1:
            result += rubbish
    return result
        

print(reverse_for_dummies("", "X"))
# <prazdny retezec>
print(reverse_for_dummies("ONMEJATEJOLSEH", "X"))
# HXEXSXLXOXJXEXTXAXJXEXMXNXO
print()


# Napiste funkci, ktera vrati novy retezec, ve kterem bylo kazde pismenko
# zdvojeno.
# duplication("PYTHON") => PPYYTTHHOONN


def duplication(text: str) -> str:
    result = ""
    for i in range(len(text)):
        result = result + text[i]*2 
    return result

print(duplication("Ahoj"))

# Napiste funkci, ktera dostane dva retezce a vrati ty znaky, ktere jsou na
# shodnych pozicich stejne.
# string_intersection("ZIRAFA", "KARAFA") => RAFA
# string_intersection("PES", "KOCKA") => (prazdny retezec)
# string_intersection("KOCKA", "PES") => (prazdny retezec)


def string_intersection(left: str, right: str) -> str:
    result = ""
    for i in range(min(len(left), len(right))):
        if left[i] == right[i]:
            result  += left[i]
    return result

print(string_intersection("ZIRAFA", "KARAFA"))

# Napiste funkci, ktera vrati, zda je retezec palindromem. Palindromem je
# takove slovo ci veta, ktera ma pri cteni v libovolnem smeru stejny vyznam,
# napriklad nepotopen ci jelenovi pivo nelej (muzete predpokladat, ze
# mezery v retezci nejsou)..
# palindrom("JELENOVIPIVONELEJ") => True


def palindrom(text: str) -> bool:
    for i in range(len(text)//2):
        if text[i] != text[-1 - i]:
            return False
    return True
            
print(palindrom(""))

# Kazdy znak A-Z ma hodnotu 1-26 (diakritiku a velikost pismen pro tento
# priklad ignorujte, predpokladejte, ze jsou vsechna velka). Napiste funkci,
# ktera spocita a vrati hodnotu vlozeneho
# retezce (slova).
# word_value("AHOJ") => 34


def word_value(text: str) -> int:
    value = 0
    for i in range(len(text)):
        value += ord(text[i]) - ord("A") + 1
    return value

print(word_value("AHOJ"))

########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_duplication_in = ("", "a", "PYTHON", "tESt")
ib113_duplication_out = ("", "aa", "PPYYTTHHOONN", "ttEESStt")


def ib113_test_duplication():
    print("Testovani funkce duplication: ", end="")
    failure = False

    for i in range(len(ib113_duplication_in)):
        res = duplication(ib113_duplication_in[i])
        if not isinstance(res, str):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu str, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_duplication_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_duplication_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_duplication_out[i]))
            break

    if not failure:
        print("OK")


ib113_string_intersection_in = (("ZIRAFA", "KARAFA"), ("PES", "KOCKA"),
                                ("", ""), ("AB", "AB"), ("KOCKA", "PES"))
ib113_string_intersection_out = ("RAFA", "", "", "AB", "")


def ib113_test_string_intersection():
    print("Testovani funkce string_intersection: ", end="")
    failure = False

    for i in range(len(ib113_string_intersection_in)):
        res = string_intersection(ib113_string_intersection_in[i][0],
                                  ib113_string_intersection_in[i][1])
        if not isinstance(res, str):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu str, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_string_intersection_out[i]:
            failure = True
            print("NOK")
            print("Pro vstupy \"{}\" a \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_string_intersection_in[i][0],
                          ib113_string_intersection_in[i][1]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\"".format(
                ib113_string_intersection_out[i]))
            break

    if not failure:
        print("OK")


ib113_palindrom_in = ("JELENOVIPIVONELEJ", "", "AB", "ABA", "AAA", "BBC")
ib113_palindrom_out = (True, True, False, True, True, False)


def ib113_test_palindrom():
    print("Testovani funkce palindrom ", end="")
    failure = False

    for i in range(len(ib113_palindrom_in)):
        res = palindrom(ib113_palindrom_in[i])
        if not isinstance(res, bool):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu bool, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_palindrom_out[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_palindrom_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_palindrom_out[i]))
            break

    if not failure:
        print("OK")


ib113_word_value_in = ("A", "", "AHOJ", "AAA")
ib113_word_value_out = (1, 0, 34, 3)


def ib113_test_word_value():
    print("Testovani funkce word_value: ", end="")
    failure = False

    for i in range(len(ib113_word_value_in)):
        res = word_value(ib113_word_value_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_word_value_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_word_value_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_word_value_out[i]))
            break

    if not failure:
        print("OK")


# Zde muzete vkladat vlastni testy
if __name__ == "__main__":
    ib113_test_duplication()
    print()
    ib113_test_string_intersection()
    print()
    ib113_test_palindrom()
    print()
    ib113_test_word_value()
