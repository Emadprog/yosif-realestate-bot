import sqlite3
from config import Config

# دالة لإنشاء الاتصال بقاعدة البيانات
def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# إنشاء الجداول الأساسية لو مش موجودة
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # جدول العملاء
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            last_message TEXT
        )
    ''')

    # جدول العقارات
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            location TEXT,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()