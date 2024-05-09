# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()


my_cats = ["octavia"]

for cat in my_cats:
    print(f"{cat} is furry")