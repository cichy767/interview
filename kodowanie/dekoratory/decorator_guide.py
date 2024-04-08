# zaletą dekoratorów jest to, że możemy dodać do funkcji jakąś funkcjonalność bez ingerencji w jej kod
# przykładem wykorzystania ich może być np. logowanie, albo zapisywanie jakichś informacji do bazy danych

def startstop(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        func(*args, **kwargs)
        print("Finished!")

    return wrapper


def roll():
    print("Rolling on the floor laughing XD")


# roll = startstop(roll)
# roll()


@startstop
def roll():
    print("Rolling on the floor laughing XD")


# roll()


def startstop(arg):
    def startstop_wrapper(func):
        def wrapper(*args, **kwargs):
            print(f"Starting... {arg}")
            result = func(*args, **kwargs)
            print("Finished!")
            return result

        return wrapper

    return startstop_wrapper


@startstop('decorator!')
def roll():
    print("Rolling on the floor laughing XD")


roll()
