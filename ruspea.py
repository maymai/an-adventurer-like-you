 # Russian Peasant algorithm
import time


CASHE = {}

def ruspeas(x, y):
    key = (x, y)
    if key in CASHE:
        total = CASHE[key]
    else:
        num1 = x
        num2 = y
        total = 0
        while num1 > 0:
            if num1 % 2 != 0:
                total += num2
            num1 = int(num1 / 2)
            num2 = num2 * 2
        CASHE[key] = total
        return total

def test_ruspeas():
    a = 37
    b = 26
    stime = time.time()
    print(ruspeas(a, b))
    print("Time taken: %s miliseconds" %(time.time() - stime))
    assert ruspeas(a, b) == a * b
    assert ruspeas(b, a) == a * b

test_ruspeas()
test_ruspeas()
print(ruspeas(53, 99))
