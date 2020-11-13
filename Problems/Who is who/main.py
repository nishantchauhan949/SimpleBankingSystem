class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


def main():
    valkyrie = Angel()
    print(valkyrie.color)
    print(valkyrie.feature)
    print(valkyrie.home)

    lucifer = Demon()
    print(lucifer.color)
    print(lucifer.feature)
    print(lucifer.home)


main()