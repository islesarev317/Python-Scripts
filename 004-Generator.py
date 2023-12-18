# Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
# Python provides generator functions as a convenient shortcut to building iterators.

def get_gen(word):
    for symbol in word:
        yield symbol


gen = get_gen("Hello")
print(next(gen))  # => H
print(next(gen))  # => e


for s in gen:
    print(s)  # => l l o
