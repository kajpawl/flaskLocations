import os
from dotenv import load_dotenv
from pathlib import Path

from flask import Flask, render_template, request, abort
from models import db, User
from forms import SignupForm

base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
load_dotenv(env_file)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)

app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
            new_user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)

            user_with_existing_email = User.query.filter(User.email == form.email.data).first()
            if user_with_existing_email is not None:
                abort(409, description=f'User with email {form.email.data} already exists.')

            db.session.add(new_user)
            db.session.commit()
            return 'Success!'
    elif request.method == 'GET':
        return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
