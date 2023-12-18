# --- 1) Summary ---

def summary():
    result = 0
    for i in range(10):
        print("i =", i)
        param = yield result
        result += param
        print("param =", param)
        print("result =", result)


print("1) Summary:")
g = summary()
print(">>>", g.send(None))
print("---")
print(">>>", g.send(6))
print("---")
print(">>>", g.send(9))


# --- 2) Average ---

def init(func):
    def inner(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


@init
def average():
    count = 0
    summ = 0
    result = None

    while True:
        try:
            x = yield result
        except StopIteration:
            break
        else:
            count += 1
            summ += x
            result = round(summ / count, 2)

    return result


print("1) Average:")
g = average()
print(">>>", g.send(5))
print(">>>", g.send(6))
try:
    g.throw(StopIteration)
except StopIteration as e:
    print(">>>", e.value)
