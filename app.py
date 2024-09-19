from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ ФБ Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <ol>
                <li><a href="/lab1">Первая лабораторная</a></li>
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
    return '''
<!doctype html>
<html>
    <head>
        <title>Цой Ольга Дмитриевна, Лабораторная работа 1</title>
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


