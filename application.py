from flask import Flask, request, render_template

from core import bank_repository

app = Flask(__name__)
brepo = bank_repository.BankRepository()


@app.route('/')
def index():
    global brepo
    return render_template('index.html', banks=brepo.get_all())


@app.route('/bank/<int:bank_id>', methods=['GET', 'POST'])
def bank(bank_id):
    if request.method == 'GET':
        return render_template('bank.html', bank_id=bank_id, bank=brepo.get(bank_id))
    elif request.method == 'POST':
        updated_bank = bank_repository.Bank(request.form['name'])
        return str(request.form['name'])


if __name__ == '__main__':
    app.run()
