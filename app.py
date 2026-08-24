from flask import Flask, render_template


# створення застосунку
app = Flask(__name__)


# route - декоратор, який обробляє маршрути
@app.route('/')
@app.route('/welcome')
def welcome():
    # render_template - функція для відображення HTML-файлів
    return render_template('welcome.html')


# запуск додатку
app.run(debug=True)