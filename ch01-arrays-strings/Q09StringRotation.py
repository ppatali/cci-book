def StringRotation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    return True if string2 in string1 + string1 else False
    