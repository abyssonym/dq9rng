seed = None


def rand():
    global seed
    seed = (seed * 0x5d588b656c078965) + 0x269ec3
    seed = seed & 0xFFFFFFFFFFFFFFFF
    return seed >> 32


def rand_with_seed(myseed):
    myseed = (myseed * 0x5d588b656c078965) + 0x269ec3
    myseed = myseed & 0xFFFFFFFFFFFFFFFF
    return myseed


def percentage(value):
    return value * 100.0 / (2 << 31)


def reverse_percentage(percentage):
    return int(percentage * (2 << 31) / 100.0)


def test_rand():
    seed = raw_input("Initial seed (in hex)? ")
    seed = int(seed, 0x10)
    while True:
        value = rand()
        print "%x" % seed
        print "%s%%" % percentage(value)
        raw_input("... ")


def rand_search(low, high, number=None, depth=None):
    initial_seeds = range(0x100000)
    chains = [[i] for i in initial_seeds]
    successes = []
    done = False
    counter = 0
    while True:
        for c in chains:
            prev = c[-1]
            iterated = rand_with_seed(prev)
            c.append(iterated)
            if low <= (iterated >> 32) <= high:
                successes.append(list(c))
            if number is not None and len(successes) >= number:
                done = True
                break
        counter += 1
        if depth is not None and counter >= depth:
            break
        if done:
            break
    return successes

if __name__ == "__main__":
    low = reverse_percentage(0.95)
    high = reverse_percentage(0.96)
    print "%x %x" % (low, high)
    print ["%x" % j for j in rand_search(low, high, number=1)[0]]
    initials = rand_search(low, high, depth=1)
    for i in initials:
        print ["%x" % j for j in i], percentage(i[-1] >> 32)
    print len(initials)
