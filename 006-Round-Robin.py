def get_gen_1(word):
    for symbol in word:
        yield symbol.upper()


def get_gen_2(limit):
    for i in range(limit):
        yield i


g1 = get_gen_1("Hello")
g2 = get_gen_2(8)
tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        result = next(task)
        print(result)
        tasks.append(task)
    except StopIteration:
        pass
