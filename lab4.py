from flask import Blueprint, render_template, request, make_response, redirect, url_for
lab4 = Blueprint('lab4', __name__)


@lab4.route ("/lab4/")
def lab():
    return render_template("lab4.html")

@lab4.route ("/lab4/div-form")
def div_form():
    return render_template("div-form.html")

@lab4.route ("/lab4/div", methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('div.html', error='Оба поля должны быть заполнены')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 / x2
    return render_template('div.html', x1=x1, x2=x2, result=result)

@lab4.route("/lab4/add", methods=['POST'])
def add():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x1 = int(x1) if x1 else 0
    x2 = int(x2) if x2 else 0
    result = x1 + x2
    return render_template('div.html', operation="суммирования", x1=x1, x2=x2, result=result)

@lab4.route("/lab4/multiply", methods=['POST'])
def multiply():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x1 = int(x1) if x1 else 1
    x2 = int(x2) if x2 else 1
    result = x1 * x2
    return render_template('div.html', operation="умножения", x1=x1, x2=x2, result=result)

@lab4.route("/lab4/subtract", methods=['POST'])
def subtract():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('div.html', error="Оба поля должны быть заполнены для вычитания")
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('div.html', operation="вычитания", x1=x1, x2=x2, result=result)

@lab4.route("/lab4/power", methods=['POST'])
def power():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('div.html', error="Оба поля должны быть заполнены для возведения в степень")
    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0 and x2 == 0:
        return render_template('div.html', error="Оба значения не могут быть равны нулю для возведения в степень")
    result = x1 ** x2
    return render_template('div.html', operation="возведения в степень", x1=x1, x2=x2, result=result)

tree_count = 0  

@lab4.route("/lab4/tree", methods=["GET", "POST"])
def tree():
    global tree_count
    if request.method == "POST":
        operation = request.form.get("operation")
        if operation == "plant":
            tree_count += 1
        elif operation == "cut" and tree_count > 0:
            tree_count -= 1
        return redirect(url_for("lab4.tree")) 
    return render_template("tree.html", tree_count=tree_count)

if __name__ == "__main__":
    lab4.run(debug=True)





# Список пользователей
users = [
    {"username": "alex", "password": "123", "name": "Алексей Иванов", "gender": "мужской"},
    {"username": "bob", "password": "456", "name": "Борис Петров", "gender": "мужской"},
    {"username": "anna", "password": "789", "name": "Анна Смирнова", "gender": "женский"}
]

@lab4.route("/lab4/login/", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")
    error = None

    # Проверка на пустые поля
    if not username:
        error = "Не введён логин!"
    elif not password:
        error = "Не введён пароль!"

    # Проверка логина и пароля
    if not error:
        for user in users:
            if user["username"] == username and user["password"] == password:
                return render_template("rrr.html", name=user["name"])

        # Ошибка если логин или пароль неверны
        error = "Неверный логин и/или пароль!"

    # Возвращаем пользователя на страницу логина с сохранённым логином и сообщением об ошибке
    return render_template("login.html", error=error, username=username)


# Добавляем маршрут для страницы регистрации
@lab4.route("/lab4/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
        
        # Проверка на пустые поля
        if not username or not password or not name:
            error = "Все поля должны быть заполнены!"
            return render_template("register.html", error=error)

        # Проверка, что логин уникален
        for user in users:
            if user["username"] == username:
                error = "Пользователь с таким логином уже существует!"
                return render_template("register.html", error=error)
        
        # Добавляем нового пользователя
        users.append({"username": username, "password": password, "name": name, "gender": "не указан"})
        return redirect(url_for("login"))

    return render_template("register.html")


@lab4.route("/lab4/fridge/", methods=["POST", "GET"])
def fridge():
    if request.method == "GET":
        return render_template("fridge.html")

    temp = request.form.get("temp")
    if not temp:
        error = "Ошибка: не задана температура!"
        return render_template("fridge.html", error = error)
    elif int(temp) < -12:
        error = "Не удалось установить температуру — слишком низкое значение!"
        return render_template("fridge.html", error = error)
    elif int(temp) > -1:
        error = "Не удалось установить температуру — слишком высокое значение!"
        return render_template("fridge.html", error = error)
    elif int(temp) >= -12 and int(temp) <= -9:
        error = "Установлена температура: " + str(temp) + "°С ❆❆❆"
        return render_template("temp.html", error = error)
    elif int(temp) >= -8 and int(temp) <= -5:
        error = "Установлена температура: " + str(temp) + "°С ❆❆"
        return render_template("temp.html", error = error)
    else:
        error = "Установлена температура: " + str(temp) + "°С ❆"
        return render_template("temp.html", error = error)
    
@lab4.route("/lab4/offer/", methods=["POST", "GET"])
def offer():
    type_offer = request.form.get("type_offer")
    if request.method == "GET":
        return render_template("offer.html")
    
    weight = request.form.get("weight")
    if not weight:
        error = "Не введён вес!"
        return render_template("offer.html", error = error)
    elif int(weight) <= 0:
        error = "Неверное значение веса!"
        return render_template("offer.html", error = error)
    elif int(weight) > 500:
        error = "Такого объёма сейчас нет в наличии!"
        return render_template("offer.html", error = error)
    elif str(type_offer) == "zerno":
        error = "Выберите зерно!"
        return render_template("offer.html", error = error)
    elif int(weight) <= 500 and int(weight) >= 50:
        weight = int(weight)
        prices = {
        'yach': 12000,
        'oves': 8500,
        'psh': 8700,
        'poz': 14000
        }
        price_per_ton = prices[type_offer]
        total_price = weight * price_per_ton
        total_price *= 0.9

        if type_offer == "yach":
            type_offer = "ячмень"
        elif type_offer == "psh":
            type_offer = "пшеница"
        elif type_offer == "poz":
            type_offer = "рожь"
        else:
            type_offer = "овес"

        return render_template("offer_conf%.html", total_price = total_price, type_offer = type_offer, weight = weight)
    else:
        weight = int(weight)
        prices = {
        'yach': 12000,
        'oves': 8500,
        'psh': 8700,
        'poz': 14000
        }
        price_per_ton = prices[type_offer]
        total_price = weight * price_per_ton

        if type_offer == "yach":
            type_offer = "ячмень"
        elif type_offer == "psh":
            type_offer = "пшеница"
        elif type_offer == "poz":
            type_offer = "рожь"
        else:
            type_offer = "овес"

        return render_template("offer_conf.html", total_price = total_price, weight = weight, type_offer = type_offer)

