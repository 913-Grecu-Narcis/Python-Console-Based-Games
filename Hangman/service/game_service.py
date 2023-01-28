from repository.file_repository import FileRepo
import random


class Service:
    def __init__(self, file_repo: FileRepo):
        self.__repo = file_repo
        self.__revealed_letters = []
        self.__guesses = []
        self.__mistakes = 0
        self.__sentence = ''

    def add_sentence(self, sentence: str):
        words = sentence.split()

        if len(words) < 1:
            raise ValueError('Sentence must have at least one word!')

        for word in words:
            if len(word) < 3:
                raise ValueError('Each word must have at least 3 letters!')

        self.__repo.add(sentence)

    def start_game(self):
        # reset if played previously
        self.__revealed_letters = []
        self.__guesses = []
        self.__mistakes = 0

        sentence = random.choice(self.__repo.get_all())
        self.__sentence = sentence
        words = sentence.split()

        for word in words:
            self.__revealed_letters.append(word[0])
            self.__revealed_letters.append(word[-1])

        return self.make_hangman_sentence(sentence)

    def make_hangman_sentence(self, sentence):
        hangman_style_sentence = ''

        for ch in sentence:
            if ch in self.__revealed_letters or ch == ' ':
                hangman_style_sentence += ch

            else:
                hangman_style_sentence += '_'

        return hangman_style_sentence

    def make_guess(self, letter):
        if letter in self.__revealed_letters or letter not in self.__sentence or letter in self.__guesses:
            self.__mistakes += 1
            return

        self.__revealed_letters.append(letter)
        self.__guesses.append(letter)

    def check_for_end(self):
        if self.__mistakes == 7:
            return -1

        sentence = self.make_hangman_sentence(self.__sentence)

        if '_' in sentence:
            return 0

        return 1

    def get_sentence(self):
        return self.__sentence

    def get_hangman(self):
        hangman = 'hangman'
        return hangman[:self.__mistakes]
