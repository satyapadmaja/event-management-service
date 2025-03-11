from flask import Flask
from config import Config
from models.event_model import db
from controllers.event_controller import event_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(event_controller)

    return app

if __name__ == '__main__':
    app = create_app()
    print("App created.")
    with app.app_context():
        db.create_all()
        print("Database tables created.")
    app.run(debug=True)