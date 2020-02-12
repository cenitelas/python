def check():
    text = input(">>>")
    keys = ["class","def", "pass", "with", "import", "for", "in" , "as", "if" , "elif", "else"]
    types = ["type","bool", "str", "int", "float", "null", "dict" , "list", "tuple"]
    if len(text)>0:
        if(len(text)>2 and text[0]=="_" and text[1]=="_" and text[2].isalpha()):
            print("OK: так называют приватные идентификаторы")
            check()

        if(len(text)>1 and text[0]=="_" and text[1].isalpha()):
            print("OK: так называют protected идентификаторы")
            check()

        if(text.upper()==text and text[0].isalpha() and text.isupper()):
            print("OK: так называют константы")
            check()    

        if(text.upper()[0]==text[0] and text[0].isalpha() and text.swapcase()!=text):
            print("OK: так называют классы")
            check()
        
        if(text.lower()==text and text[0].isalpha() and text.swapcase()==text):
            print("OK: так называют переменные")
            check()

        if(text.lower()==text and keys.count(text)>0):
            print("NOK: ключевое слово")
            check()
        
        if(types.count(text)>0):
            print("NOK: типы данных")
            check()

        print("NOK: Значение")

    check()

check()