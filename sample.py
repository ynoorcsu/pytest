#! venv/bin/python

def square(x):
    try:
        return x**2
    except TypeError:
        raise 
