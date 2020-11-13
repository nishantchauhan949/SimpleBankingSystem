# start a RockBand here
class RockBand:
    genre = 'rock'
    key_instruments = ['electric guitar', 'drums']
    n_members = 4


def main():
    pink_floyd = RockBand()
    print(pink_floyd.genre)
    print(pink_floyd.n_members)
    print(pink_floyd.key_instruments)


main()
