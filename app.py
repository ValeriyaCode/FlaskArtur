from flask import Flask, render_template
from random import randint, choice

# створення застосунку
app = Flask(__name__)


# route - декоратор, який обробляє маршрути
@app.route('/')
@app.route('/welcome')
def welcome():
    # render_template - функція для відображення HTML-файлів
    return render_template('welcome.html', name='Artur')


@app.route('/students')
def students():
    all_students = ['Artur', 'Lera']
    return render_template('students.html', students=all_students)


@app.route('/gift')
def gift():
    is_lucky = choice([True, False])
    discount = randint(1000, 10_000)

    return render_template('gift.html', is_lucky=is_lucky, discount=discount)


# запуск додатку
app.run(debug=True)