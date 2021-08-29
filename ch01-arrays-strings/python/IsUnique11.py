def IsUnique(str) -> bool:
    if not str:
        return False
    
    #Assuming string only contains ASCII char set
    TOTAL_UNIQUE_CHARS = 128
    if len(str) > TOTAL_UNIQUE_CHARS:
        return False
    
    #charFlags = [False] * TOTAL_UNIQUE_CHARS
    charFlags = [False for i in range(TOTAL_UNIQUE_CHARS)] #Alternative with list comprehension
    for c in str:
        if charFlags[ord(c)]:
            return False
        charFlags[ord(c)] = True
    
    return True



