seed = None


def rand():
    global seed
    seed = (seed * 0x5d588b656c078965) + 0x269ec3
    seed = seed & 0xFFFFFFFFFFFFFFFF
    return (seed >> 32) & 0xFFFFFFFF


def percentage(value):
    return value * 100.0 / (2 << 31)


if __name__ == "__main__":
    seed = raw_input("Initial seed (in hex)? ")
    seed = int(seed, 0x10)
    while True:
        value = rand()
        print "%x" % seed
        print "%s%%" % percentage(value)
        raw_input("... ")
