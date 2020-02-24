import re
def check(text):
    pattern = "[a-zA-Z0-9]{1,}\.[a-zA-Z0-9]{1,}\.[a-zA-Z0-9]{1,}"
    print(re.findall(pattern, text))

check("asdaasd As.2SD3.ru asdas ww.dd.2Aa.kz asdasd ww.ru asdasd")


