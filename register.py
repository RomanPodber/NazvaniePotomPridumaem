from flask import Flask, redirect, render_template
from data import db_session
from data.users import User
from data.users import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'z_k.,k._zyltrc_kbwtq'

def connecting(func):
    db_session.global_init("db/userstable.sqlite")
    def some_func():
       func()

@connecting
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

app.run()

if __name__ == '__main__':
    connecting()