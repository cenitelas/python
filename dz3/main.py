currency = {"kzt":{"usd":380},"usd":{"kzt":0.02}}
def check():
    text = input(">>>")
    params = text.split(" ");
    try:
        if len(params) == 3:
            result = float(params[0])*currency[params[1].lower()][params[2].lower()]
            print(result)
        if len(params) == 4:
            if currency.get(params[1]):
                currency[params[3]]=float(params[2])
            else:
                currency[params[1]]={params[3]:float(params[2])}
            print("OK")
    except:
        print("Нет такой валютной пары")
    check()


