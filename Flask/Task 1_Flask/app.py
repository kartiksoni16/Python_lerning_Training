from flask import Flask
from routes import app_routes
from auth import auth
from config import Config
from models import db, User
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(app_routes)
app.register_blueprint(auth)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=9000)
