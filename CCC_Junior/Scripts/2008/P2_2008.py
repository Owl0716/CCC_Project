
def main():
    button_number = 0
    playlist = ['A','B','C','D','E']
    while not button_number == 4:
        button_number = int(input('Button number:'))
        number_of_presses = int(input('Number of presses:'))
        playlist = rule(button_number,number_of_presses,playlist)
    str_play = ''
    for i in playlist:
        str_play += i
        str_play +=' '
    print(str_play)


def rule(button_num,num_presses,playlist):
    n_playlist = []
    for i in range(num_presses):
        if button_num == 1:
            for f in range(1,len(playlist)):
                n_playlist.append(playlist[f])
            n_playlist.append(playlist[0])
            return n_playlist
        elif button_num == 2:
            n_playlist.append(playlist[-1])
            for g in range(len(playlist)-1):
                n_playlist.append(playlist[g])

            return n_playlist
        elif button_num == 3:
            n = playlist[1]
            n_playlist.append(playlist[1])
            n_playlist.append(playlist[0])
            for k in range(2,len(playlist)):
                n_playlist.append(playlist[k])

            return n_playlist
        elif button_num == 4:
            return playlist
if __name__ == '__main__':
    main()