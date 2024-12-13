from flask import Blueprint, render_template, request, session, jsonify

lab6 = Blueprint('lab6', __name__, template_folder='templates')

# Предопределенные данные о кабинетах
offices = [{"number": i, "tenant": "", "price": 1000 + (i % 3) * 500} for i in range(1, 11)]

@lab6.route('/lab6/')
def lab_6():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    method = data.get('method')
    id = data.get('id')

    if method == 'info':
        return jsonify({'jsonrpc': '2.0', 'result': offices, 'id': id})

    login = session.get('login', 'test_user')  # Используем "test_user" для тестирования
    if not login:
        return jsonify({'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'Unauthorized'}, 'id': id})

    if method == 'booking':
        office_number = data.get('params')
        for office in offices:
            if office['number'] == office_number:
                if office['tenant']:
                    return jsonify({'jsonrpc': '2.0', 'error': {'code': 2, 'message': 'Already booked'}, 'id': id})
                office['tenant'] = login
                return jsonify({'jsonrpc': '2.0', 'result': 'Office booked successfully', 'id': id})

    if method == 'cancellation':
        office_number = data.get('params')
        for office in offices:
            if office['number'] == office_number:
                if not office['tenant']:
                    return jsonify({'jsonrpc': '2.0', 'error': {'code': 4, 'message': 'Office not booked'}, 'id': id})
                if office['tenant'] != login:
                    return jsonify({'jsonrpc': '2.0', 'error': {'code': 5, 'message': 'Not your office'}, 'id': id})
                office['tenant'] = ''
                return jsonify({'jsonrpc': '2.0', 'result': 'Cancellation successful', 'id': id})

    return jsonify({'jsonrpc': '2.0', 'error': {'code': -32601, 'message': 'Method not found'}, 'id': id})
