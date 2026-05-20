from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATABASE = "users.db"

# Создание базы
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()

init_db()

# Получить пользователей
@app.route("/users", methods=["GET"])
def get_users():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    conn.close()

    users = []

    for row in rows:
        users.append({
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "age": row[4]
        })

    return jsonify(users)

# Добавить пользователя
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (first_name, last_name, email, age)
        VALUES (?, ?, ?, ?)
    """, (
        data["first_name"],
        data["last_name"],
        data["email"],
        data["age"]
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "User added"
    })

# Удалить пользователя
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "User deleted"
    })

# Вывести время и статус
@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "ONLINE",
        "time": datetime.now().strftime("%H:%M:%S")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

