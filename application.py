from flask import Flask, request, render_template
from core import bank_repository

app = Flask(__name__)
bank_repository = bank_repository.BankRepository()


@app.route("/")
def hello():
    return render_template('index.html', name=bank_repository.)


@app.route("/bank/<int:bank_id>", methods=['GET', 'POST'])
def bank(bank_id):
    if request.method == 'GET':
        return str(bank_id)
    elif request.method == 'POST':
        return str(request.data)


if __name__ == "__main__":
    app.run()
