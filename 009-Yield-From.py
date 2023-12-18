def reader():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        yield ">>> %s" % i


def reader_wrapper_1(g):
    for v in g:
        yield v


def reader_wrapper_2(g):
    yield from g


wrap = reader_wrapper_2(reader())
for line in wrap:
    print(line)
