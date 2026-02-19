from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///learning_platform.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
from shared.database.db_init import db
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'module1.login'

# Import models after db is initialized
from shared.database import models

# Import module routes
from module1_ui.backend.routes import module1_bp
from module2_user_data.backend.routes import module2_bp
from module3_ai_processing.backend.routes import module3_bp
from module4_voice_visual.backend.routes import module4_bp
from module5_reminders.backend.routes import module5_bp

# Register blueprints
app.register_blueprint(module1_bp)
app.register_blueprint(module2_bp)
app.register_blueprint(module3_bp)
app.register_blueprint(module4_bp)
app.register_blueprint(module5_bp)

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
