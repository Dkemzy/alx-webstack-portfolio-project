from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from forms import ExpenseForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Expense('{self.title}', '{self.category}', {self.amount}, {self.date})"


@app.route('/')
def home():
    all_expenses = Expense.query.all()
    return render_template('home.html', expenses=all_expenses)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(title=form.title.data, category=form.category.data,
                          amount=form.amount.data, date=form.date.data)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('home'))
    form.date.data = datetime.now()
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
