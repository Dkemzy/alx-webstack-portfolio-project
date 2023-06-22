from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from datetime import datetime
from __init__ import create_app, db
from forms import ExpenseForm
from models import Expense

main = Blueprint('main', __name__)


@main.route('/')# home page that return 'index'
def index():
    return render_template('index.html')


@main.route('/profile')  # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/expenses')
@login_required
def expenses():
    all_expenses = Expense.query.all()
    return render_template('expenses.html', expenses=all_expenses)

@main.route('/calculate', methods=['GET','POST'])
@login_required
def calculate():
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('calculate.html')
    else:
        total_income = float(request.form['total_income'])
    
    savings = total_income * 0.2
    wants = total_income * 0.3
    necessities = total_income * 0.5
    
    return render_template('result.html', necessities=necessities, wants=wants, savings=savings)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(title=form.title.data, category=form.category.data,
                          amount=form.amount.data, date=form.date.data)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('main.expenses'))
    form.date.data = datetime.now()
    return render_template('add.html', form=form)


@main.route("/update/<int:expense_id>", methods=['GET', 'POST'])
@login_required
def update(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    form = ExpenseForm()
    # if the form is validated and submited, update the data of the item
    # with the data from the field
    if form.validate_on_submit():
        expense.title = form.title.data
        expense.category = form.category.data
        expense.amount = form.amount.data
        expense.date = form.date.data
        db.session.commit()
        return redirect(url_for('main.expenses'))
        # populate the field with data of the chosen expense
    elif request.method == 'GET':
        form.title.data = expense.title
        form.category.data = expense.category
        form.amount.data = expense.amount
        form.date.data = expense.date
    return render_template('add.html', form=form, title='Edit Expense')


@main.route("/delete/<int:expense_id>", methods=['POST'])
@login_required
def delete(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('main.expenses'))

@main.route("/aboutus",methods=['GET'])
@login_required
def aboutus():
    return render_template('aboutus.html')

@main.route("/contactus",methods=['GET','POST'])
@login_required
def contactus():
    return render_template('contactus.html')

@main.route("/faqs",methods=['GET'])
@login_required
def faqs():
    return render_template('faqs.html')

app = create_app()  # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
