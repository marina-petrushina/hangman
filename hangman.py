import random
def hangman(word):
    alphabet = ["а", "б", "в",
            "г", "д", "е",
            "ё", "ж", "з",
            "и", "й", "к",
            "л", "м", "н",
            "о", "п", "р",
            "с", "т", "у",
            "ф", "х", "ц",
            "ч", "ш", "щ",
            "ъ", "ы", "ь",
            "э", "ю", "я"]
    print("Привет! Поиграем в Виселицу?\n")
    wrong = 0
    stages = ['',
              '_______         ',
              '|               ',
              '|      |        ', 
              '|      0        ',
              '|     /|\       ',
              '|     / \       ',
              '|               '
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print("Угадай слово из {} букв.".format(len(word)))
    used_letters = set()
    while wrong < len(stages) - 1:
        print('\n')
        msg = "Напиши букву: "
        char = input(msg)
        if char in rletters:
            print("\nУгадал.\n")
            for letter in rletters:
                if letter == char:
                    cind = rletters.index(char)
                    board[cind] = char
                    rletters[cind] = '$'
                    used_letters.add(char)
        elif char in used_letters:
            print("\nЭту букву ты уже угадывал.\n")
        elif char in alphabet:        
            wrong += 1
            print("\nВ  слове нет такой буквы.\n")
        else:
            wrong += 1
            print("\nПромах, в следующий раз пиши букву русского алфавита.\n")
        print((' '.join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Ты выиграл! Было загадано слово: ")
            print(' '.join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: e]))
        print("Ты проиграл! Было загадано слово: {}.".format(word))

words = ["кот", "собака", "попугай", "рыба", "хомяк"]
number = random.randint(0, len(words) - 1)
hangman(words[number])
