from flask import Flask, request, render_template

from core import banks

app = Flask(__name__)
brepo = banks.BankRepository()


@app.route('/')
def index():
    global brepo
    return render_template('index.html', banks=brepo.get_all())


@app.route('/bank/<int:bank_id>', methods=['GET', 'POST'])
def bank(bank_id):
    if request.method == 'GET':
        return render_template('bank.html', bank_id=bank_id, bank=brepo.get(bank_id))
    elif request.method == 'POST':
        # pa = banks.Preset(request.form['pa.l1'], request.form['pa.l2'], request.form['pa.l3'], request.form['pa.l4'], request.form['pa.kd'])
        # updated_bank = banks.Bank(request.form['name'])
        return str(request.form['name'])


if __name__ == '__main__':
    app.run()
