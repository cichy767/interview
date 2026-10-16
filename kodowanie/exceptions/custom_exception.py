class MyException(Exception):
    pass


class ValidationError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors


if __name__ == "__main__":
    # Celowa demonstracja własnego wyjątku i jego przechwycenia.
    try:
        raise MyException('MY OWN EXCEPTION!')
    except MyException as exc:
        print(f"Przechwycono MyException: {exc}")
