import pytest
from flask import Flask
from sqlalchemy import inspect
from models import db
from database import init_db

@pytest.fixture
def app():
    # Cria uma aplicação Flask para teste
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    return app

def test_init_db(app):
    # Verifica se o banco de dados foi inicializado corretamente
    with app.app_context():
        init_db(app)
        inspector = inspect(db.engine)
        # Verifica se a lista de tabelas está vazia
        assert inspector.get_table_names() == []
