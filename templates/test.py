from app import db,app,Expense
def database():
    with app.app_context():
        db.create_all()
        expense_1 = Expense(title='MacBook', category='Work', amount=1500)
        expense_2 = Expense(title='Headphone', category='Person', amount=100)
        expense_3 = Expense(title='Netflix', category='Service', amount=15)
        expense_4 = Expense(title='Spotify', category='Person', amount=30)
        db.session.add(expense_1)
        db.session.add(expense_2)
        db.session.add(expense_3)
        db.session.add(expense_4)
        db.session.commit()
        Expense.query.all()
database()
