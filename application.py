from flask import Flask, request, render_template

from core import banks

app = Flask(__name__)
bank_repository = banks.BankRepository()


@app.route('/')
def index():
    global bank_repository
    return render_template('index.html', banks=bank_repository.get_all())


@app.route('/bank/<int:bank_id>')
def show_bank(bank_id):
    return render_template('bank.html', bank_id=bank_id, bank=bank_repository.get(bank_id))


@app.route('/bank/<int:bank_id>', methods=['POST'])
def update_bank(bank_id):
    pa = banks.Preset('pa.l1' in request.form, 'pa.l2' in request.form, 'pa.l3' in request.form, 'pa.l4' in request.form,
                      'pa.kd' in request.form)
    pb = banks.Preset('pb.l1' in request.form, 'pb.l2' in request.form, 'pb.l3' in request.form, 'pb.l4' in request.form,
                      'pb.kd' in request.form)
    pc = banks.Preset('pc.l1' in request.form, 'pc.l2' in request.form, 'pc.l3' in request.form, 'pc.l4' in request.form,
                      'pc.kd' in request.form)
    bank_repository.update(bank_id, banks.Bank(request.form['name'], pa, pb, pc))
    return 'saved'

if __name__ == '__main__':
    app.run()
