from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

# Inisialisasi Database
with app.app_context():
    db.create_all()
    
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

# Endpoint untuk menambahkan user baru
@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

# Endpoint untuk mendapatkan semua user
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'id': user.id, 'name': user.name, 'email': user.email}
        output.append(user_data)
    return jsonify({'users': output})

# Endpoint untuk mendapatkan user berdasarkan ID
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_data = {'id': user.id, 'name': user.name, 'email': user.email}
    return jsonify({'user': user_data})

# Endpoint untuk mengupdate user
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

# Endpoint untuk menghapus user
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)
