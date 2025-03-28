print("hello-world")

def area(a, b, *args):
    c = list(args)
    print(c)
    d = 0
    if c.__len__() == 1:
        print("one__true")
    elif c.__len__() > 1:
        for index, i in enumerate(c):
            x, y = c[index]
            d = area(x, y) + d
            print("d", d)
    if c.__len__() == 0:
        return a * b
    elif c.__len__() > 0:
        return a * b + d

def main():
    c = area(4, 5, (3,3), (4,2))
    print(c)

main()