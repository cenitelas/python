import re


def check(text):
    pattern = r'(?<![\.-])\b(([a-z0-9]|-[^-])+\.){2}[A-z]{1,}\b(?!(\.\S|-))'
    print('\nResult:')
    for r in re.finditer(pattern, text, re.IGNORECASE):
        print(r.group())


check(input('Enter text:'))
