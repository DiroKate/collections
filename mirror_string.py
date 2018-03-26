def mirrorEqual(str, flag):
    size = 1
    while True:
        try:
            if flag - size < 0:
                break
            left = str[flag - size]
            right = str[flag + size + 1]
        except Exception:
            break
        if left == right:
            size += 1
        else:
            break
    return size, str[flag - size + 1:flag + size + 1]

def mirrorString(str):
    flags = []
    result = {}

    for i in xrange(len(str)-1):
        if str[i] == str[i+1]:
            flags.append(i)

    maxLen = 0
    theMirror = ''

    for flag in flags:
        size,mirror = mirrorEqual(str, flag)
        if size > maxLen:
            theMirror = mirror
            maxLen = size
    return theMirror, maxLen


if __name__ == '__main__':
    print(mirrorString('aaaaaaaaaaa'))
    print(mirrorString('123321123321'))
    print(mirrorString('123654456987'))
    print(mirrorString('213fgaw87ry823ugbr2y3trgruagef76rqgfy29q3rasdbfias76yr8q23rgisdahf87qt53b'))
