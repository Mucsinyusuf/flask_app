from flask import Flask, request, jsonify
from models import db, User
from flask_migrate import Migrate
 
app = Flask(__name__,)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
migrate = Migrate(app,db)




@app.route("/members")
def index ():
    return "hello"


@app.route('/user_manager', methods=['GET','POST','PATCH','DELETE'])

def manage_users():
    if request.method == 'GET':
        users = User.query.all()
        users_list = []
        for user in users:
            users_list.append({
            "id": user.id,
            "usrname": user.username,
            "email": user.email
        })
        return jsonify(users_list)
    elif request.method == 'POST':

    

    # data = request.get_json()

        username = request.form.get('username')
        email = request.form.get('email')

        if not username or not email:
            return jsonify({"error": "Username and email are required"}), 400
    
        all_ready_added=User.query.filter_by(email=email).first()
        if all_ready_added:
            return jsonify({"error": "User Already added"})
 

        new_user = User(username=username, email=email)

        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully!", "user": {"username": username, "email": email}}), 201




if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)