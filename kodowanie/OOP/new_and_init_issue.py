# metoda __new__ musi zwracać obiekt
# metoda init musi zwrazać None
"""
Zadanie: Metoda __new__ jest statyczną metodą fabryczną (chociaż formalnie nie jest deklarowana jako statyczna),
co oznacza, że jest odpowiedzialna za tworzenie nowych instancji obiektów.
Jej zadaniem jest zwrócenie nowej instancji obiektu danej klasy.

Sygnatura: Pierwszym argumentem __new__ jest zawsze klasa (cls), dla której ma zostać stworzona instancja.
Metoda ta może również przyjmować dodatkowe argumenty, które następnie mogą być przekazane do __init__ dla zainicjalizowania nowego obiektu.

Dziedziczenie: __new__ jest szczególnie użyteczna w klasach niemutowalnych (takich jak str, int, tuple) i w metaprogramowaniu.
W przypadku klas mutowalnych rzadko jest konieczna modyfikacja jej zachowania, ale w przypadku dziedziczenia po klasach niemutowalnych może być niezbędna do stworzenia instancji.

Zwracanie wartości: Metoda __new__ musi zwrócić instancję klasy (lub innej klasy).
Jeżeli __new__ nie zwróci instancji klasy, dla której jest wywoływana, to metoda __init__ dla tego obiektu nie zostanie wywołana.

Wywołanie __init__: Jeśli __new__ zwróci instancję klasy, dla której jest wywoływana,
Python automatycznie wywoła metodę __init__ tej klasy, aby zainicjalizować nowo utworzony obiekt, przekazując instancję jako pierwszy argument self,
a następnie pozostałe argumenty przekazane do konstruktora klasy.
"""


class FlightPlan:
    def __new__(cls, callsign, dep, des):
        if dep == des:
            cls.is_local = True
        obj = object.__new__(cls)
        return obj

    def __init__(self, callsign, dep, des):
        self.callsign = callsign
        self.dep = dep
        self.des = des
        # return self


# fp1 = FlightPlan('asd', 'a', 'a')
fp1 = FlightPlan('asd', 'a', 'd')

print(fp1.is_local)
