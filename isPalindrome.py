def isPalindrome(n):
    if n < 0:
        return False
    stringN = str(n)
    firstIndex = 0
    lastIndex = len(stringN) - 1
    while (firstIndex < lastIndex):
        if not stringN[firstIndex] == stringN[lastIndex]:
            return False
        firstIndex += 1
        lastIndex -= 1
    return True


print(isPalindrome(-1221))
