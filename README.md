# wordle_solver
CLI program to solve Wordle (https://wordle.danielfrg.com/)

## Install Requirements
`$ pip install -r requirements.txt`

## Run the code
`$ python3 wordle_solver.py`

### How it works
To start off, the program will always recommends the word `alero`.
Once you've put said word on the web, you'll need to insert the status of each letter (from left to right) on the terminal (green: in word and in place; yellow: in word but not in place; black: not in word):

`g -> if the letter "a" appears in green.`

`y -> if the letter "a" appears in yellow.`

`b -> if the letter "a" appears in black.`

And so on with each letter of the first inserted word: `alero`.
Once the status of each of the letters in the word "alero" is shown, the program will recommend a second new word.

After inserting said word into the web, you'll now need to insert the current status of the letters in the program as they appear in [wordle.danielfrg.com](https://wordle.danielfrg.com)

Now, repeat until you win :)

## DEMO
https://user-images.githubusercontent.com/24664579/161899170-84f25376-79e2-444f-9551-41c5df897277.mov

