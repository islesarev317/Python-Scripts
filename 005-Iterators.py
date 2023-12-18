# 1) CREATE:
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

class SpellWord:

    def __init__(self, word):
        self.word = word
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.word):
            symbol = self.word[self.i]
            self.i += 1
            return symbol
        raise StopIteration


iterator = SpellWord("Hello")
print(next(iterator))  # => H
print(next(iterator))  # => e

for s in iterator:  # it causes iter(iterator)
    print(s)  # => l l o


# 2) USAGE:

my_tuple = ("apple", "banana", "cherry")
my_it = iter(my_tuple)

print(next(my_it))  # => apple
print(next(my_it))  # => banana

for fruit in my_it:
    print(fruit)  # => cherry

for fruit in my_tuple:  # we can do this, because it causes iter(my_tuple)
    print(fruit)  # => apple banana cherry
