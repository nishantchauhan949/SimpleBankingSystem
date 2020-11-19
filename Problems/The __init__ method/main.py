# class NotWordError(Exception):
#     def __init__(self, word):
#         self.message = word + " is not a word, sorry!"
#         super().__init__(self.message)
#

def check_word(word):
    for letter in word:
        if letter == '0':
            raise NotWordError(word)
    return word


def error_handling(word):
    try:
        print(check_word(word))
    except NotWordError as nwe:
        print(nwe)

#
# if __name__ == '__main__':
#     error_handling('spu0dd')
