from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/lab2/example')
def example():
    name, number, group, course = 'Цой Ольга', 2, 'ФБИ-23', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
        ]
    books = [
        {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'Исторический роман', 'pages': 1200},
        {'author': 'Федор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 600},
        {'author': 'Антуан де Сент-Экзюпери', 'title': 'Маленький принц', 'genre': 'Фантазия', 'pages': 100},
        {'author': 'Габриэль Гарсиа Маркес', 'title': 'Сто лет одиночества', 'genre': 'Магический реализм', 'pages': 450},
        {'author': 'Джордж Оруэлл', 'title': '1984', 'genre': 'Дистопия', 'pages': 328},
        {'author': 'Достоевский Ф.', 'title': 'Идиот', 'genre': 'Роман', 'pages': 700},
        {'author': 'Гарри Поттер', 'title': 'Гарри Поттер и философский камень', 'genre': 'Фэнтези', 'pages': 223},
        {'author': 'Джейн Остин', 'title': 'Гордость и предубеждение', 'genre': 'Роман', 'pages': 432},
        {'author': 'Марк Твен', 'title': 'Приключения Гекльберри Финна', 'genre': 'Приключения', 'pages': 366},
        {'author': 'Джон Р. Р. Толкин', 'title': 'Властелин колец', 'genre': 'Фэнтези', 'pages': 1178}
        ]
    return render_template('example.html', name=name, number=number, 
    group=group, course=course, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/memes/')
def memes():
    return render_template('memes.html')


@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return f"""
<!doctype html>
<html>
    <head>
        <title>НГТУ ФБ Лабораторные работы</title>
        <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <ol>
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2">Вторая лабораторная</a></li>
            </ol>
        </main>

        <footer>
            &copy; Цой Ольга, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return f'''
<!doctype html>
<html>
    <head>
        <title>Цой Ольга Дмитриевна, Лабораторная работа 1</title>
        <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов Werkzeug,
            а также шаблонизатор Jinja2. Относится к категории так называемых
            микрофреймворков — минималистичных каркасов веб-приложений,
            сознательно предоставляющих лишь самые базовые возможности.
        </p>
        
        <p>
            <a href="/menu">Меню</a>
        </p>

        <h1>Реализованные роуты</h1>

        <ul>
            <li><a href="/lab1/oak">/lab1/oak - дуб</a></li>
            <li><a href="/lab1/student">/lab1/student - студент</a></li>
            <li><a href="/lab1/python">/lab1/python - python</a></li>
            <li><a href="/lab1/cats">/lab1/cats - cats</a></li>
        </ul>
 
        <footer>
            &copy; Цой Ольга, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@app.route("/lab1/oak")
def oak():
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="{url_for('static', filename='oak.jpg')}">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
    </head>
    <body>
        <h1>Цой Ольга Дмитриевна</h1>
        <img src="{url_for('static', filename='Логотип.jpeg')}" width="300" height="200">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return f'''
<!doctype html>
<html>
<head>
        <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
    </head>
    <body>
        <h1>Python</h1>
        <p>
            Python — это язык программирования, который широко используется в интернет-приложениях, 
            разработке программного обеспечения, науке о данных и машинном обучении.
            Разработчики используют Python, потому что он эффективен, прост в изучении и работает на разных платформах.
        </p>

        <p>
            Для него написано множество фреймворков: FastAPI, Flask, Tornado, Pyramid, 
            TurboGears, CherryPy и, самый популярный, Django. Ещё на Python пишут парсеры для сбора информации с веб-страниц.
        </p>

        <p>
            Минусом является его малое быстродействие и недостаточные возможности статического анализа кода. 
            Эти проблемы взаимосвязаны, и решение последней автоматически откроет дорогу для решения первой.
        </p>
        <img src="{url_for('static', filename='Питон.png')}">
    </body>
</html>
'''

@app.route("/lab1/cats")
def cats():
    return f'''
<!doctype html>
<html>
<head>
        <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
    </head>
    <body>
        <h1>Про котиков</h1>
        <p>
            Люди, когда заводят кота, представляют его с определенным набором качеств: одни хотят игривого и активного,
            другие ласкового, а третьи — ненавязчивого и спокойного. Было бы удобно, если бы характер зависел, например, 
            от пола питомца — чтобы можно было примерно представлять, каким будет любимец. Однако коты устроены гораздо 
            сложнее, поэтому давайте разбираться, отличается ли темперамент кошек от котов.
        </p>

        <p>
            Поэтому при выборе питомца обращайте внимание, как он ведет себя в вашем присутствии. Также смотрите на 
            обстановку, в которой он рос. Если в питомнике кошек держат в чистоте, уделяют им внимание и следят 
            за здоровьем — больше вероятности, что малыши социализированы и обладают стабильной нервной системой.
        </p>

        <p>
           Каждая кошка обладает своим уникальным характером. Он может зависеть не только от пола, но и породы, 
           воспитания и других факторов. 
        </p>
        <img src="{url_for('static', filename='Коты.jpeg')}">
    </body>
</html>
'''
