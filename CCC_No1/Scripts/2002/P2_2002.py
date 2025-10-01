import math

vowels = ["a", "e","i", "o","u","y"]

def check(word):
    new = word
    for letter in word:
        if letter.isalpha():
            if not letter in vowels:
                i = word.index(letter)
                if word[i+1:i+3] == 'or':
                    new = word[:i+1] + 'our' + word[i+3:]
        else:
            continue

    return new

def main():
    print('Enter words to be translated:')
    while 1==1:
        word = (input(''))
        if word == 'quit!':
            break
        if len(word) < 4:
            print(word)
            continue
        word = check(word)
        print(word)
    print(1234)

if __name__ == '__main__':
    main()