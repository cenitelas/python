currency = {"kzt": {"usd": 380}, "usd": {"kzt": 0.02}}

def check():
    while True:
        text = input(">>>")
        params = text.split(" ")
        try:
            if len(params) == 3:
                result = float(params[0]) * currency[params[2].lower()][params[1].lower()]
                print(result)
            if len(params) == 4:
                if currency.get(params[3].lower()):
                    currency[params[3].lower()][params[1].lower()] = float(params[2])
                else:
                    currency[params[3].lower()] = {params[1].lower(): float(params[2])}
                if currency.get(params[1].lower()):
                    currency[params[1].lower()][params[3].lower()] = float(params[0])/float(params[2])
                else:
                    currency[params[1].lower()] = {params[3].lower(): float(params[0])/float(params[2])}

                print("OK")
        except:
            print("Нет такой валютной пары")

check()