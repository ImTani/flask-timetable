from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('api/central_schedule.db')

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    initials = request.args.get('initials')
    current_day = datetime.now().strftime('%A')
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT period, class FROM schedule WHERE initials=? AND day=? ORDER BY period', 
              (initials, current_day))
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/api/schedule', methods=['POST'])
def add_schedule():
    data = request.get_json()
    initials = data['initials']
    classes = data['classes']
    day = data['day']
    conn = connect_db()
    c = conn.cursor()
    for period, class_name in enumerate(classes, start=1):
        c.execute('INSERT INTO schedule (initials, period, class, day) VALUES (?, ?, ?, ?)', 
                  (initials, period, class_name, day))
    conn.commit()
    conn.close()
    return '', 204

@app.route('/api/schedule/clear', methods=['POST'])
def clear_database():
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM schedule')
    conn.commit()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
