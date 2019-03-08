import random

gus = ""
answer = random.randint(0, 10000)
guss_number = 0

while gus != answer:
    gus = int(input("Hads Bezan: "))
    guss_number += 1
    if answer < gus <= answer + 40:
        print("Vaii Kheyli Nazdiki Javab Kochik Tare")
    elif gus >= answer + 40:
        print("Kheyli Dori Javab Kochik Tare")
    elif answer > gus >= answer - 40:
        print("Vaii kHeyli Nazdiki Javab Bozorg Tare")
    elif gus <= answer - 40:
        print("Kheyli Dori Javab Bozorg Tare")
else:
    print("Afaaariiiin , Toye", guss_number, "Bar Talash Bordi")
