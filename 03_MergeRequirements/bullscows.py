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

if __name__ == '__main__':
    pass