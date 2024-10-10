from flask import Flask, jsonify, request
from database import init_db
from models import User, db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    init_db(app)

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        new_user = User(username=data['username'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'user registred'})
    
    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
