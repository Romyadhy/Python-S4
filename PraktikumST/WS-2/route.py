from main import main, User, db
from flask import  jsonify, request


@main.route('/', methods=['GET'])
def hello_world():
    return "Tes Klient Swerverere coooo"

# Endpoint untuk menambahkan user baru
@main.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

# Endpoint untuk mendapatkan semua user
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}
        output.append(user_data)
    return jsonify({'users': output})

# Endpoint untuk mendapatkan user berdasarkan ID
@main.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_data = {'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}
    return jsonify({'user': user_data})

# Endpoint untuk mengupdate user
@main.route('/user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.name = data['name']
    user.email = data['email']
    user.age = data['age']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

# Endpoint untuk menghapus user
@main.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})