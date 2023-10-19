# codenames-solver

## User Guide

Codenames works off of a 5x5 grid of 25 cards. Imagine they are labeled left to right as such:

| card 0  	| card 1  	| card 2  	| card 3  	| card 4  	|
|---------	|---------	|---------	|---------	|---------	|
| card 5  	| card 6  	| card 7  	| card 8  	| card 9  	|
| card 10 	| card 11 	| card 12 	| card 13 	| card 14 	|
| card 15 	| card 16 	| card 17 	| card 18 	| card 19 	|
| card 20 	| card 21 	| card 22 	| card 23 	| card 24 	|

The `teller` will see the game card showing which cards their team should guess. Encode the associated card numbers into hints with:

```bash
$ python3 solver.py --dictionary_file dict.txt --cards 0,4,9,10,13,15,18,19    
hint:  nonpraedial
```
The guesser can then decode the associated card numbers from the hint word with:
```bash
$ python3 solver.py --dictionary_file dict.txt --hint nonpraedial --hint_size 8
guess cards: 
0
4
9
10
13
15
18
19
```

## Prose
[Codenames](https://codenames.game/) (sometimes also called Codewords), is a game where `tellers` give single-word hints in an effort to prompt `guessers` to select either 8 or 9 cards for a 5x5 grid of 25 word cards.

Some might see the combinatorics problem here: `nCr(25, 8) = 1,081,575` and `nCr(25, 9) = 2,042,975`

This means that a game of Codenames can be solved by numbering each word in a dictionary with an intended outcome.
`tellers` encode the solution by ordering the possible outcomes of the board and serving a word which is ordered correspondingly.
`guessers` decode the solution by ordering the possible outcomes and finding the rank of the word in the dictionary.

This does require that the `tellers` and `guessers` agree on what counts as a `word`. Various places have different dictionaries.

In order to encode the maximum possible number of board positions, users will want to choose a dictionary that is sufficiently large. The larger the dictionary, the more card can be encoded into a guess.
Some good dictionary options are:
| Dictionary | Size | Maximum Board Positions Guaranteed |
|---------	|---------	|---------	|
| https://github.com/dwyl/english-words/tree/master | 466,550 words | 6: `nCr(25, 6) = 177,100` |
| https://www-personal.umich.edu/~jlawler/wordlist.html | 69,903 words | 5: `nCr(25, 5) = 53,130` |

The size of the first dictionary means that about half of game positions can be encoded in one hint, and the rest can be solved in two.

In the current solution, if the board position seeking to be encoded is too far down the combinations order that it can't fit into the dictionary, the script exits and requests the user to fit fewer cards into this hint.

Solving the game in one hint for every board position requires a dictionary of 1,081,575 words for 8 cards and 2,042,975 for 9 cards.
