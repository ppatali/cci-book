def CheckPermutation(str1, str2) -> bool:
    if not str1 or not str2 or len(str1) != len(str2):
        return False
    
    TOTAL_UNIQUE_CHARS = 128
    charCount = [0 for i in range(TOTAL_UNIQUE_CHARS)]

    for c in str1:
        charCount[ord(c)] += 1
    
    for c in str2:
        index = ord(c)

        charCount[index] -= 1
        if charCount[index] < 0:
            return False
    
    return True

