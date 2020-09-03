class Player:
    # moze posiadac jawny konstruktor z polami, 
    # ustwiającymi obiekt,czyli byt posiadający wałściwości klasy
    # poprzez obiekt, mozmey dostawac sie do metod klasy i jej walsciwosci.
    def __init__(self, name, email, points):
        print("tworzę playera")
        self.name = name
        self.email = email
        self.points = points
    
    # używamy sami, gdy chcemy uchornić się przed memory leak. 
    # garbage collector powinień usunąć obiekt, ale robimy to ręcznie dla pewności.
    def __del__(self): 
        print("kasuję playera")

    def __int__(self):
        return 1024    # liczba dowolna, tylko aby z obiektu mozna bylo zwrocic jakąś liczbę.

    def __len__(self): # to co wyżej, ale z umowną długością obiektu.
        return 1

    def __str__(self):
        return (f"player:{self.name},{self.email},{self.points}")

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

