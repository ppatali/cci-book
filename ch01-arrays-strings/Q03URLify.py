from typing import List

def URLify(val: List[str], truelength: int) -> List[str]:
    if not val:
        return val
    
    spaceCount = 0
    for i in range(truelength):
        if val[i] == ' ':
            spaceCount += 1
    
    index = truelength + spaceCount * 2
    
    if index > len(val):
        return val

    # for i in range(truelength-1, 0, -1):
    for i in reversed(range(truelength)):
        if val[i] == ' ':
            # val[index - 1] = '0'
            # val[index - 2] = '2'
            # val[index - 3] = '%'
            val[index-3:index] = "%20"
            index -= 3
        else:
            val[index - 1] = val[i]
            index -= 1
    
    return val