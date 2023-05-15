from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_email):
    return User.get(user_email)

class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def get(user_email):
        with open('login.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['email'] == user_email:
                    return User(user['email'])
        return None
    
    def is_active(self):
        return self.active
    
    def is_authenticated(self):
        emailInput = request.form.get("email")
        passwordInput = request.form.get("password")
        with open("login.json", "r") as f:
            users = json.load(f)
        for user in users:
            if check_password_hash(user["password"], passwordInput) and user["email"] == emailInput:
                return True
        return False
    
    def get_id(self):
        return self.email

@app.route('/login', methods=['GET', 'POST'])
def login():
    with open("login.json", "r") as f:
        existing_user = json.load(f)

    users = existing_user
    newUser = {}

    if request.method == 'POST':
        nameReg = request.form.get("nickname")
        emailReg = request.form.get("reg-email")
        pwd1Reg = request.form.get("pwd1")
        
        if not nameReg:
            userEmail = User.get(emailInput)
            if userEmail:
                login_user(userEmail)
                return redirect(url_for("index"))
            flash('Incorrect email or password')
            return redirect(url_for('login'))
        
        else:
            hashPwd = generate_password_hash(pwd1Reg, method="sha256")
            newUser['name'] = nameReg
            newUser['password'] = hashPwd
            newUser['email'] = emailReg
            users.append(newUser)
            with open("login.json", "w") as file:
                json.dump(users, file, indent=4)
            return redirect(url_for('index'))

    return render_template("login.html")
## End of Login & Register Code