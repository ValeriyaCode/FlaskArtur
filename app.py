from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'something'

# GET - відображає сторінки з потрібними даними
# POST - отримання даних від клієнта та їх обробка

@app.route('/', methods=['GET', 'POST'])
def main():
    # POST (отримання даних з форми)
    if request.method == 'POST':
        user_password = request.form.get('password')
        print(f'user_password: {user_password}')

        # flash-повідомлення, доступні до наступного запиту
        flash('You logged in!')

        # redirect - перенаправляє на певну сторінку з методом GET
        # url_for - дозволяє вказати назву функції, яка обробляє певний маршрут
        return redirect(url_for('main'))

    # GET (отримання даних через args з адресного рядку)
    user_search = request.args.get('search')
    return render_template('index.html', search=user_search)

app.run(debug=True)
