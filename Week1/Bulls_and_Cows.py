class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = Counter(secret)
        guess_count = Counter(guess)
        bulls = count = cows = 0;

        for i in range(len(secret)):
            digit = secret[i]
            if digit in secret_count.keys() and \
                                digit in guess_count.keys():
                    count += min(secret_count.pop(digit) , guess_count.pop(digit))

            if secret[i] == guess[i]:
                bulls += 1

        cows = count - bulls
        return str(bulls) + "A" + str(cows) + "B"
        
