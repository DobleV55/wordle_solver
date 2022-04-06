import os
import click
import re

progress = {'g':{}, 'y':[], 'b':[]}

def main():
    print('Use this word to start: alero')
    print('Use green (g) if the letter exists and is in the correct place')
    print('Use yellow (y) if the letter exist but is in the wrong place.')
    print('Use black (b) if the letter doesnt exist in the word.')
    possible_word = 'alero'
    # ask user if the word works
    for _ in range(6):
        possible_word = get_possible_word(possible_word)
        print(possible_word)

def get_possible_word(possible_word):
    for index in range(len(possible_word)):
        result = click.prompt(possible_word[index], type=click.Choice(['g','y','b']))
        if result != 'g':
            progress[result].append(possible_word[index])
        else:
            progress['g'][index] = possible_word[index]

    #create green filter
    green_filter = '01234'
    for index in range(5):
        if progress['g'].get(index):
            green_filter = green_filter.replace(str(index), progress['g'][index])

    # search words by filtering
    f = open('final_es.txt', 'r')
    words = f.readlines()
    possible_words = []
    green_filter_string = re.sub(r'\d', '.', green_filter)
    for word in words:
        yellow_filter = True
        green_filter = True
        black_filter = False
        for letter in list(progress['g'].values()):
            if letter in progress['b']:
                progress['b'].remove(letter)
        if progress['b']:
            black_filter = re.search(f"{progress['b']}", word)
        if green_filter_string != '^.....':
            green_filter = re.search(f"^{green_filter_string}", word)
        if progress['y']:
            yellow_filter = re.search(f"{progress['y']}", word)
        #black_filter = not black_filter
        if not black_filter and green_filter and yellow_filter:
            possible_words.append(word.split()[0])
    return possible_words[0]


if __name__ == "__main__":
    main()
