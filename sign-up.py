from flask import Flask, jsonify, request
import bcrypt

app       = Flask(__name__)
app.users = {}
app.id_count = 1


@app.route("/sign-up",methods=['POST'])
def sign_up():
    new_user                 =request.json
    new_user['password'] = bcrypt.hashpw(
        new_user['password'].encode('UTF-8'),
        bcrypt.gensalt()
    )
    new_user_id           = app.database.execute(text("""
    INSERT INTO users (
        name,
        email,
        profile,
        hashed_password
    ) VALUES (
        :name,
        :email,
        :profile,
        :password
    )
    """), new_user). lastrowid
    new_user_info = get_user(new_user_id)
    return jsonify(new_user_info)

    
    row = current_app.database.execute(text("""
    SELECT
        id,
        name,
        email,
        profile
    FROM users
    WHERE id = :user_id
    """), {
        'user_id' = :new_user_id
    }).fetchone()

    created_user = {
        'id'     :row['id'],
        'name'   :row['name']
        'email'  :row['row']
        'profile':row['profile']
    } if row else None

    return jsonify(created_user)