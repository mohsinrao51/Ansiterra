from flask import Flask, request, jsonify
from datetime import datetime
from db import get_db_connection

app = Flask(__name__)

@app.route('/visitors', methods=['POST'])
def add_visitor():
    data = request.json
    name = data.get('name')
    visit_time = datetime.now()

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO visitors (name, visit_time) VALUES (%s, %s)", (name, visit_time))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Visitor added'}), 201

@app.route('/visitors', methods=['GET'])
def get_visitors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM visitors")
    visitors = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(visitors), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

