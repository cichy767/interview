"""
Metaklasa w Pythonie to klasa klas, czyli taki typ, który definiuje jak klasy są tworzone.
W przeciwieństwie do klas, które definiują zachowanie obiektów (instancji), metaklasy definiują zachowanie klas.
Dzięki temu, metaklasy pozwalają na zaawansowaną modyfikację lub rozszerzenie klas podczas ich definicji.

Jak działają metaklasy?
W Pythonie, kiedy tworzysz klasę, Python używa metaklasy do jej utworzenia. Domyślną metaklasą jest type,
ale można ją zmienić, aby dostosować proces tworzenia klasy. Właściwie, każda klasa w Pythonie jest instancją swojej metaklasy.
"""


class TypedMeta(type):
    def __new__(cls, name, bases, dct):
        # Tutaj można dodać logikę sprawdzającą lub modyfikującą dct
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=TypedMeta):
    pass
