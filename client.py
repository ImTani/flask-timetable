import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
import json

SERVER_URL = 'https://flask-timetable.vercel.app/'

def fetch_schedule(initials):
    current_day = datetime.now().strftime('%A')
    response = requests.get(f'{SERVER_URL}/api/schedule', params={'initials': initials})
    return response.json()

def display_schedule():
    initials = initials_entry.get().upper()
    schedule = fetch_schedule(initials)
    
    for row in tree.get_children():
        tree.delete(row)
    
    for row in schedule:
        tree.insert("", "end", values=row)

def add_schedule(initials, classes, day):
    data = {
        'initials': initials,
        'classes': classes,
        'day': day
    }
    requests.post(f'{SERVER_URL}/api/schedule', json=data)

def clear_database():
    requests.post(f'{SERVER_URL}/api/schedule/clear')

clear_database()
add_schedule("RS", ["6A", "7B", "8C", "9A", "FREE", "5B", "6C", "7D"], "Monday")
add_schedule("MS", ["5D", "6E", "7F", "8A", "FREE", "9B", "10C", "11D"], "Monday")
add_schedule("AS", ["5E", "6F", "FREE", "8B", "10A", "9C", "10D", "11E"], "Monday")

add_schedule("RS", ["5D", "6E", "7F", "8A", "FREE", "9B", "10C", "11D"], "Tuesday")
add_schedule("AS", ["5E", "6F", "FREE", "8B", "10A", "9C", "10D", "11E"], "Tuesday")

app = tk.Tk()
app.title("Teacher Schedule")

tk.Label(app, text="Enter your initials:").grid(row=0, column=0, padx=10, pady=10)
initials_entry = tk.Entry(app)
initials_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(app, text="Show Schedule", command=display_schedule).grid(row=0, column=2, padx=10, pady=10)

columns = ("Period", "Class")
tree = ttk.Treeview(app, columns=columns, show='headings')
tree.heading("Period", text="Period")
tree.heading("Class", text="Class")
tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

current_day = datetime.now().strftime('%A')

app.mainloop()
