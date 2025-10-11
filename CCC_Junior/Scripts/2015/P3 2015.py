def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines
def main():
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelsnum = [0,4,8,14,20]
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lines = read_file('../../TextFiles/2015/P3_Input_2015')
    Pig_latin = []
    word = list(lines[0])
    for i in range(len(word)):
        if word[i] in consonant:
            indexc = consonant.index(word[i])
            indexa = alphabet.index(word[i])
            min_distance =1000
            test_var = ''

            Pig_latin.append(word[i])


            for f in range(len(vowelsnum)):
                if abs(vowelsnum[f] - indexa) < min_distance:
                    min_distance = abs(vowelsnum[f] - indexa)

            if indexa + min_distance < 26:
                if alphabet[indexa + min_distance] in vowels:
                    Pig_latin.append(alphabet[indexa + min_distance])
                else:
                    Pig_latin.append(alphabet[indexa - min_distance])
            elif indexa - min_distance > 0:
                if alphabet[indexa - min_distance] in vowels:
                    Pig_latin.append(alphabet[indexa - min_distance])
                else:
                    Pig_latin.append(alphabet[indexa + min_distance])






            #find the consontant
            if not word[i] == 'z':
                Pig_latin.append(consonant[indexc+1])
            else:
                Pig_latin.append('z')

        else:
            Pig_latin.append(word[i])
    string_Pig_latin = ''
    for i in range(len(Pig_latin)):
        string_Pig_latin += Pig_latin[i]
    print(string_Pig_latin)


if __name__ == '__main__':
    main()