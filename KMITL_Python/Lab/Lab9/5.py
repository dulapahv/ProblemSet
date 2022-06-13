def isAnagram(String1, String2):
    if sorted(String1) == sorted(String2):
        return True
    return False