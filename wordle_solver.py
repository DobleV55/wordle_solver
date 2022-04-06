from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
from pprint import pprint
from examples import custom_style_2

import click

import os
import re

progress = {'g':{}, 'y':[], 'b':[]} # global variable
used_words = []

def menu():
    options = ['Wordle ES (wordle.danielfrg.com)', 'Latin Wordle (wordle.latindictionary.io)', 'NY Times Wordle (nytimes.com/games/wordle)','Wordle org (wordlegame.org)']
    
    questions = [
        {
            'type': 'list',
            'name': 'answer',
            'message': 'Which Wordle are you playing?',
            'choices': options
        }
    ]

    answers = prompt(questions, style=custom_style_2)
    if answers['answer'] == 'Wordle ES (wordle.danielfrg.com)':
        return 'es'
    elif answers['answer'] == 'Latin Wordle (wordle.latindictionary.io)':
        return 'latin'
    elif answers['answer'] == 'NY Times Wordle (nytimes.com/games/wordle)' or answers['answer'] == 'Wordle org (wordlegame.org)':
        return 'en'
    return

def best_word_to_start(game_type):
    best_words_to_start = {'es':'alero','en':'opera','latin':'aesti'}
    return best_words_to_start[game_type]

def main():
    
    game_type = menu()

    used_words.append(best_word_to_start(game_type))
    print('Use green (g) if the letter exists and is in the correct place')
    print('Use yellow (y) if the letter exist but is in the wrong place.')
    print('Use black (b) if the letter doesnt exist in the word.')
    print('')
    print(f'Use this word to start: {used_words[-1]}')
    # ask user if the word works, six are the maximum possible tries.
    for _ in range(6):
        get_possible_word(game_type, used_words[-1])
        print(f'Used words: {used_words}')
        print(used_words[-1])

def get_possible_word(game_type, possible_word):
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
    f = open(f'word_lists/{game_type}.txt', 'r')
    words = f.readlines()
    possible_words = []
    green_filter_string = re.sub(r'\d', '.', green_filter)
    for word in words:
        word = word.split()[0]
        yellow_filter = True
        green_filter = True
        black_filter = False

        # remove green and yellow letters from black letters
        green_and_yellow_letters = list(progress['g'].values()) + progress['y']
        for letter in green_and_yellow_letters:
            if letter in progress['b']:
                progress['b'].remove(letter)
        if progress['b']:
            black_filter = re.search(f"{progress['b']}", word)
        if green_filter_string != '^.....':
            green_filter = re.search(f"^{green_filter_string}", word)
        if progress['y']:
            yellow_filter = re.search(f"{progress['y']}", word)
        #black_filter = not black_filter
        #if word == 'comma':
            #import pdb; pdb.set_trace()
        if not black_filter and green_filter and yellow_filter:
            possible_words.append(word)
    print(f'Possible_words: {possible_words}')

    for word in possible_words:
        if word not in used_words:
            print(f'Word: {word}')
            used_words.append(word)
            return


if __name__ == "__main__":
    main()
