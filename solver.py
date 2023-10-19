from typing import List
from itertools import combinations
import math

import argparse


def encode(cards: List[int], board: List[int], words: List[str]) -> str:
    # TODO devise a method for quick access
    index = 0
    for comb in combinations(board, len(cards)):
        if len(set(comb).intersection(cards)) == len(cards):
            return words[index]
        index += 1
        if index > len(words):
            raise Exception("This dict is too small to hold this hint, lower the number of cards and try again")

            

def decode(hint: str, hint_size: int, board: List[int], words: List[str]) -> List[int]:
    # TODO devise a method for quick access
    index = 0
    for comb in combinations(board, hint_size):
        if words[index] == hint:
            return comb
        index += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_size", type=int, default=25)
    parser.add_argument("--cards", type=str, help="comma seperated card numbers to encode in a word from the dictionary file")
    parser.add_argument("--dictionary_file", type=str, help="path to txt file")
    parser.add_argument("--hint", type=str, help="encoded hint word")
    parser.add_argument("--hint_size", type=int, help="Number of guesses you have for this hint")
    args = parser.parse_args()
    board = [x for x in range(args.board_size)]
    words = []
    for line in open(args.dictionary_file,'r').readlines():
        words.append(line.strip())
    if args.hint is not None:
        result = decode(args.hint, args.hint_size, board, words)
        print("guess cards: ")
        for card in result:
            print(card)
    elif args.cards is not None:
        cards = [int(x) for x in args.cards.split(",")]
        comb_size = math.comb(len(board), len(cards))
        guesses_needed = math.ceil(comb_size / len(words))
        print("num of words: ", len(words))
        print("possible combinations: ", comb_size)
        print("max possible guesses needed: ", guesses_needed)
        print("hint: ", encode(cards, board, words))
