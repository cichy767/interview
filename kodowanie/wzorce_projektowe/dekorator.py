# Wzorzec dekorator pozwala dynamicznie dodawać nowe zachowania do obiektów poprzez umieszczenie ich w specjalnych obiektach-wrappach.
# Umożliwia rozszerzanie funkcjonalności obiektów bez modyfikacji ich kodu.

def my_decorator(func):
    def wrapper():
        print("Coś się dzieje przed wywołaniem funkcji.")
        func()
        print("Coś się dzieje po wywołaniu funkcji.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
