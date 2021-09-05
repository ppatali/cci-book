def IsOneEditAway(string1: str, string2: str) -> bool:
    
    len1 = len(string1)
    len2 = len(string2)

    if abs(len1 - len2) > 1:
        return False
    
    # Make s1 the shorter of the two string
    s1, s2 = (string1, string2) if len1 <= len2 else (string2, string1)
    
    foundDifference = False
    index1 = index2 = 0

    while index1 < len1 and index2 < len2:
        if s1[index1] != s2[index2]:
            if foundDifference:
                return False
            
            if len1 == len2:
                index1 += 1
            
            foundDifference = True
        else:
            index1 += 1
        
        index2 += 1
    
    return True
            
