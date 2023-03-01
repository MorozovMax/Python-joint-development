import random
import argparse
import urllib.request
from cowsay import cowsay, list_cows

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
        inpt = input(cowsay(
                message=prompt,
                cow=random.choice(list_cows()),
        ) + '\n')
        if valid is None:
            break
        elif inpt in valid:
            break
        else:
            print("Wrong word, use valid words from this:")
            print(valid)
    return inpt

def inform(format_string: str, bulls: int, cows: int) -> None:
    print( cowsay(
            message=format_string.format(bulls, cows),
            cow=random.choice(list_cows()),
        ))

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
    parser = argparse.ArgumentParser()
    parser.add_argument('dict', type=str)
    parser.add_argument('len', type=int, default=5, nargs='?')
    args = parser.parse_args()

    try:
        words = urllib.request.urlopen(args.dict).read().decode().split()
    except:
        try:
            words = open(args.dict, 'r').read().split()
        except:
            print(f'Wrong dictionary {args.dict}')
    words = [word for word in words if len(word) == args.len]
    print("Number of attempts: ", gameplay(ask, inform, words))
