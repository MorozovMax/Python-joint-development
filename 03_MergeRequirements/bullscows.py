import random
import sys
import urllib.request

def bullscows(guess: str, secret: str) -> (int, int):
    bulls = 0
    cows = 0
    for inx, char in enumerate(guess):
        if guess[inx] == secret[inx]:
            bulls += 1
        elif char in secret:
            cows += 1
    answer = (bulls, cows)
    return answer

def ask(prompt: str, valid: list[str] = None) -> str:
    while(True):
        print(f"{prompt}")
        inpt = input()
        if valid is None:
            break
        elif inpt in valid:
            break
        else:
            print("Wrong word, use valid words from this:")
            print(valid)
    return inpt

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    try_cnt = 0
    secret = random.choice(words)
    while(True):
        guess = ask("Введите слово: ", words)
        try_cnt += 1
        b, c = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        if c == 0 and b == len(secret):
            break
    return try_cnt

if __name__ == '__main__':
    pass