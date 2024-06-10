import sqlite3

def init_db():
    conn = sqlite3.connect('central_schedule.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS schedule (initials TEXT, period INTEGER, class TEXT, day TEXT)')
    conn.commit()
    conn.close()

def add_schedule(initials, classes, day):
    conn = sqlite3.connect('central_schedule.db')
    c = conn.cursor()
    for period, class_name in enumerate(classes, start=1):
        c.execute('INSERT INTO schedule (initials, period, class, day) VALUES (?, ?, ?, ?)', 
                  (initials, period, class_name, day))
    conn.commit()
    conn.close()

init_db()

add_schedule("RS", ["6A", "7B", "8C", "9A", "FREE", "5B", "6C", "7D"], "Monday")
add_schedule("MS", ["5D", "6E", "7F", "8A", "FREE", "9B", "10C", "11D"], "Monday")
add_schedule("AS", ["5E", "6F", "FREE", "8B", "10A", "9C", "10D", "11E"], "Monday")

add_schedule("RS", ["5D", "6E", "7F", "8A", "FREE", "9B", "10C", "11D"], "Tuesday")
add_schedule("AS", ["5E", "6F", "FREE", "8B", "10A", "9C", "10D", "11E"], "Tuesday")