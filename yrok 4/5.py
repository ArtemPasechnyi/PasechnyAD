# -- coding: utf-8 --
def cf():
    s = input("ввести строчку - ")
    if (s.count("f") == 1):
        print(s.find("f"))
    if (s.count("f") >= 2):
        print("первый индекс - ", s.find("f"))
        print("последний индекс - ", s.rfind("f"))
cf()
