from flask import Flask
from app import config

app = Flask(__name__)

app.config['DATABASE_STR'] = 'postgresql://admin:admin@localhost/pp'
if config.is_testing:
    app.config['DATABASE_STR'] = 'sqlite:///test.db'

from app.views import family_budget
from app.views import personal_budget
from app.views import user

app.register_blueprint(user.user_blueprint)
app.register_blueprint(family_budget.family_budgets_blieprint)
app.register_blueprint(personal_budget.personal_budgets_blieprint)

