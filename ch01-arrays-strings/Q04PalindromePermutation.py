from collections import Counter

def IsPalindromePermutation(input: str) -> bool:
    counter = Counter()
    oddCount = 0

    for c in input:
        c = c.lower()
        if ord('a') <= ord(c) and ord(c) <= ord('z'):
            counter[c] += 1
            if (counter[c] % 2 == 1):
                oddCount += 1
            else:
                oddCount -= 1

    return oddCount <= 1

# a version to learn lambda, map and filter function
def IsPalindromePermutationV2(input: str) -> bool:
    is_char = lambda c: ord('a') <= ord(c) and ord(c) <= ord('z')
    counter = Counter(filter(is_char, list(input.lower())))
    return sum(map(lambda c: counter[c] % 2, counter)) <= 1