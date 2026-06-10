from flask import Flask

from controllers import locadora_bp
from models import db

app = Flask(__name__, template_folder="views/templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///locadora.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(locadora_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
