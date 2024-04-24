"""
In Python, the asterisk * used in function arguments, particularly in the form def func(*, arg1, arg2):,
indicates that all arguments following the asterisk must be provided as keyword arguments.
This means that the caller of the function cannot simply rely on the positional order of the arguments
but must explicitly name each argument in the function call.
"""


def func(*, arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# Calling the function correctly
func(arg1=10, arg2=20)

# This would result in an error
# func(10, 20)
