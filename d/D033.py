# coding: utf-8


def main():
    l = input().strip().split()

    m = []
    for i in l:
        m.append(i[0])
    print(".".join(m))


if __name__ == "__main__":
    main()
