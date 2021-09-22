import datetime
def aisatuk():
    dt_now=datetime.datetime.now()
    year=dt_now.year
    month=dt_now.month
    day=dt_now.day
    hour=dt_now.hour
    minute=dt_now.minute
    print('{}/{}/{}'.format(year,month,day))
    print('{}:{}'.format(hour,minute))
    if hour>=3 and hour<=9:
        print('おはよう！、足立佳奈だよ')
    elif hour>=10 and hour<=17:
        print('こんにちは、足立佳奈だよ')
    elif hour>=18 and hour<=24:
        print('こんばんは、足立佳奈だよ')
    else:
        print('もう夜中だよ！')
