import math
def get_primes_(n):
    # Use the seive of Erastothenes
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    sqrt = round(math.sqrt(n)) + 1
    for i in range(2, sqrt):
        for j in range(i+i, n+1, i):
            primes[j] = False
    return [i for i, x in enumerate(primes) if x]

primes = get_primes_(100000)
primes_len = len(primes)
def get_primes(num):
    idx = 0
    while idx < primes_len and primes[idx] <= num:
        idx += 1
    return primes[:idx]

def get_winner(n):
    # We only need to look at the primes
    numbers = get_primes(n)
    if len(numbers) % 2 == 0:
        return 'Bob'
    else:
        return 'Alice'

def run():
    games = int(input())
    for _ in range(games):
        n = int(input())
        print(get_winner(n))

# run()

class Data():
    def __init__(self, inputs, outputs):
        self.inputs = inputs.split('\n')
        self.outputs = outputs.split('\n')
        self.idx = 0

    def input(self):
        res = self.inputs[self.idx]
        self.idx += 1
        return res

    def output(self):
        return self.outputs[self.idx - 2].strip()

def test_0():
    inputs = '''3
    1
    2
    5'''

    outputs = '''Bob
    Alice
    Alice'''
    return Data(inputs, outputs)


def test_case(num):
    inputs = open('test_cases/input{num:02d}.txt'.format(num=num), 'r').read()
    outputs = open('test_cases/output{num:02d}.txt'.format(num=num), 'r').read()
    return Data(inputs, outputs)

def test_input(test):
    games = int(test.input())
    for _ in range(games):
        n = int(test.input())
        assert get_winner(n) == test.output(), 'Should be {correct} but is {answer} for {n}'.format(
                correct=test.output(), answer=get_winner(n), n=n)

def test():
    print('1')
    test_input(test_0())
    print('2')
    test_input(test_case(4))
    print('test_1')
    test_input(test_case(1))

if __name__ == '__main__':
    test()

