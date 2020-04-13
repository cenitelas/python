import sys


def cyr2lat2cyr(ch, start):
    dic = [('А', "A"),
           ('Б', "B"),
           ('В', "V"),
           ('Г', "G"),
           ('Д', "D"),
           ('Е', "E"),
           ('Ё',"JE"),
           ('Ж',"ZH"),
           ('З', "Z"),
           ('И', "I"),
           ('Й', "Y"),
           ('К', "K"),
           ('Л', "L"),
           ('М', "M"),
           ('Н', "N"),
           ('О', "O"),
           ('П', "P"),
           ('Р', "R"),
           ('С', "S"),
           ('Т', "T"),
           ('У', "U"),
           ('Ф', "F"),
           ('Х', "KH"),
           ('Ц', "C"),
           ('Ч', "CH"),
           ('Ш', "SH"),
           ('Щ', "JSH"),
           ('Ъ', "HH"),
           ('Ы', "IH"),
           ('Ь', "JH"),
           ('Э', "EH"),
           ('Ю', "JU"),
           ('Я', "JA")]
    for a, b in dic:
        if start:
            if a == ch:
                return b
        if not start:
            if b == ch:
                return a
    return ch


def main():
    args = sys.argv[1:]
    newStr = []
    for str in args:
        checkStr = []
        for ch in str:
            checkStr.append(cyr2lat2cyr(ch.upper(), True))

        check = not "".join(checkStr) == str.upper()

        for ch in str:
            newStr.append(cyr2lat2cyr(ch.upper(), check))

    print("".join(newStr))


if __name__ == '__main__':
    main()
