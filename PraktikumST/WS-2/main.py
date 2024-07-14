from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'employees.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    age = db.Column(db.Integer)
    addres = db.Column(db.String(50))
    position = db.Column(db.String(100))
    date_hired = db.Column(db.Date)
    university = db.Column(db.String(100))
    department = db.Column(db.String(100))  
    salary = db.Column(db.Float)  

# Inisialisasi Database
with app.app_context():
    db.create_all()
    

@app.route('/', methods=['GET'])
def hello_world():
    return  render_template('tes.html')

# Create user
@app.route('/user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        date_hired = datetime.strptime(data['date_hired'], '%Y-%m-%d').date()
        new_user = User(
            name=data['name'], 
            email=data['email'], 
            age=data['age'],
            addres=data['addres'],
            position=data['position'],
            date_hired=date_hired,
            university=data['university'],
            department=data['department'],
            salary=data['salary']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added successfully'}), 201
    
    except KeyError as e:
        return jsonify({'message': 'Failed to add user. Missing key in JSON data.', 'error': str(e)}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to add user', 'error': str(e)}), 500

# Show users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id, 
            'name': user.name, 
            'email': user.email, 
            'age': user.age, 
            'addres': user.addres,
            'position': user.position,
            'date_hired': user.date_hired,
            'university': user.university,
            'department': user.department,
            'salary': user.salary
            
        }
        output.append(user_data)
    return jsonify({'users': output})

# Show user by ID/spesific
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_data = {
        'id': user.id, 
        'name': user.name, 
        'email': user.email, 
        'age': user.age, 
        'addres': user.addres,
        'position': user.position,
        'date_hired': user.date_hired,
        'university': user.university,
        'department': user.department,
        'salary': user.salary
        
    }
    return jsonify({'user': user_data})

# Update user
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.get_json()
        user = User.query.get(id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        if 'date_hired' in data:
                date_hired = datetime.strptime(data['date_hired'], '%Y-%m-%d').date()
                user.date_hired = date_hired
            
        user.name = data['name']
        user.email = data['email']
        user.age = data['age']
        user.addres = data['addres']
        user.position = data['position']
        # user.date_hired = data_hired
        user.university = data['university']
        user.department = data['department']
        user.salary = data['salary']
        
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    except KeyError as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update user. Missing key in JSON data.', 'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update user', 'error': str(e)}), 500

# Delete user
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

# Main
if __name__ == "__main__":
    app.run(debug=True)
