class MyException(Exception):
    pass


class ValidationError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors


# raise ValidationError('Error!', 'error')

raise MyException('MY OWN EXCEPTION!')
