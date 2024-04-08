"""
Wzorzec obserwator definiuje zależność typu jeden-do-wielu między obiektami,
tak że gdy jeden obiekt zmienia swój stan, wszystkie jego zależne są o tym powiadamiane i aktualizowane automatycznie.
"""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class ObserverA:
    def update(self, subject):
        print("ObserverA: Otrzymano aktualizację!")


class ObserverB:
    def update(self, subject):
        print("ObserverB: Otrzymano aktualizację!")


subject = Subject()
observer_a = ObserverA()
observer_b = ObserverB()

subject.attach(observer_a)
subject.attach(observer_b)
subject.notify()
