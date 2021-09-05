from typing import Counter

def Compress(input: str) -> str:
    output = []
    count = 0
    
    for i in range(len(input)):
        count += 1
        if i + 1 == len(input) or input[i] != input[i+1]:
            output.append(input[i] + str(count))
            count = 0

    outputstr = ''.join(output)

    return outputstr if len(outputstr) < len(input) else input
