
class Kalkulator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodawanie(self):
        return self.a + self.b

    def odejmowanie(self):
        return self.a - self.b

    def mnozenie(self):
        return self.a * self.b
    
    def dzielenie(self):
        return self.a / self.b
    
    def wyswietlWynik(self, wynikDzialania):
        print("\nWynik działania: ", wynikDzialania)

a = int(input("Wpisz pierwszą liczbę: "))
b = int(input("Wpisz drugą liczbę: "))

kalkulator = Kalkulator(a, b)

wyborDzialania = input("\nWybierz rodzaj dzialania: \n1 - +\n2 - -\n3 - *\n4 - /\nWpisz liczbę działania: ")

if wyborDzialania == '1':
    wynikDzialania = kalkulator.dodawanie()
    kalkulator.wyswietlWynik(wynikDzialania)
elif wyborDzialania == '2':
    wynikDzialania = kalkulator.odejmowanie()
    kalkulator.wyswietlWynik(wynikDzialania)
elif wyborDzialania == '3':
    wynikDzialania = kalkulator.mnozenie()
    kalkulator.wyswietlWynik(wynikDzialania)
elif wyborDzialania == '4':
    wynikDzialania = kalkulator.dzielenie()
    kalkulator.wyswietlWynik(wynikDzialania)
else:
    print("Nie ma takiej operacji!")

del kalkulator