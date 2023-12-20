def charlie(x):
    for i in range(len(x)):
        x[i] = pow(i + 1, 1 / 3)


def main():
    cubed_roots = [0] * 100
    charlie(cubed_roots)
    for i in range(100):
        print(cubed_roots[i])


if __name__ == '__main__':
    main()
