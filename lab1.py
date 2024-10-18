from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1', __name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)

@lab1.route("/menu")
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

@lab1.route("/lab1")
def lab():
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

@lab1.route("/lab1/oak")
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

@lab1.route("/lab1/student")
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

@lab1.route("/lab1/python")
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

@lab1.route("/lab1/cats")
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
