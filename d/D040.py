# coding: utf-8


def main():
    l = [int((input())) for i in range(7)]

    count = 0
    for i in l:
        if i <= 30:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
