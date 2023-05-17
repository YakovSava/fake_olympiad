from faker import Faker
from random import randint

fake = Faker('ru_RU')

already_generated = []

def _get_random_name(id:str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Сертификат о прохождении конкурса за 11 класс</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }}
        .certificate {{
            width: 800px;
            height: 600px;
            margin: 0 auto;
            background-color: #f7f7f7;
            border: 10px solid #333;
            box-sizing: border-box;
            padding: 30px;
            position: relative;
        }}
        h1 {{
            margin-top: 0;
            text-align: center;
            text-transform: uppercase;
        }}
        .info {{
            margin-top: 50px;
            line-height: 1.5;
        }}
        .logo {{
            position: absolute;
            top: 30px;
            right: 30px;
        }}
        img {{
            width: 100px;
            height: auto;
        }}
    </style>
</head>
<body>
<div class="certificate">
    <div class="logo">
        <img src="images/logo.svg">
    </div>
    <h1>Сертификат</h1>
    <div class="info">
        <p>Настоящим удостоверяется, что <strong>{fake.name()}</strong></p>
        <p>завершил олимпиаду по <strong>математике</strong></p>
        <p>и успешно прошел <strong>конкурс за 11 класс</strong></p>
        <p>с результатом <strong>{randint(0, 100)} баллов из 100</strong></p>
        <p>Дата выдачи сертификата: <strong>{randint(0, 15)} мая 2023 года</strong></p>
        <p>Сайт проекта: <strong><a href="http://195.133.201.7">http://195.133.201.7</a></strong></p>
    </div>
    <div class="info">
        <p>Программа олимпиады: <strong>Олимпиадник</strong></p>
        <p>Подпись организатора: <img src="images/sign.png" width="5px" height="5px"></p>
        <p>Номерной знак сертификата: <strong>{id}</strong></p>
    </div>
</div>
</body>
</html>'''

def zero_fill(num:int) -> str:
    snum = str(num)
    while len(snum) < 6:
        snum = '0' + snum
    return snum

def main():
    for number in map(zero_fill, [randint(10, 100000) for _ in range(50)]):
        if number not in already_generated:
            with open(f'html/sertificates/{number}.html', 'w', encoding='utf-8') as file:
                file.write(_get_random_name(number))
            already_generated.append(number)

if __name__ == '__main__':
    main()