def main():
    first_word = list(input("Enter first phrase>"))
    second_word = list(input("Enter second phrase>"))
    first_word = remove_nothing(first_word)
    second_word = remove_nothing(second_word)
    if len(first_word) == len(second_word):
        for i in range(len(first_word)):
            if second_word[0] in first_word:
                second_word.pop(0)

        if len(second_word) == 0:
            print('Is an anagram.')
        else:
            print("Is not an anagram.")

    else:
        print("Is not an anagram.")


def remove_nothing(word):
    n=[]
    for i in word:
        if not i == ' ':
            n.append(i)
    return n
if __name__ == '__main__':
    main()