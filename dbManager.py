import datetime
import os
from settings import logging
import settings
import sqlite3


def is_new_db():
    return not os.path.exists(settings.DB_FILE_NAME)

def create_db(conn):
    logging.info("Creating database")
    create_schema = """
    create table data (
        key   text primary key,
        value text,
        date  datetime default current_timestamp
    );
    """
    conn.executescript(create_schema)

def insert_or_replace_data(key, value):
    is_new = is_new_db()
    with sqlite3.connect(settings.DB_FILE_NAME) as conn:
        if is_new: create_db(conn)
        now = datetime.datetime.now()
        conn.execute("insert or replace into data (key, value, date) values ('{}', '{}', '{}')".format(
                        key,
                        value,
                        now.strftime("%Y-%m-%d %H:%M:%S")))

def read_data(key):
    if is_new_db():
        with sqlite3.connect(settings.DB_FILE_NAME) as conn: create_db(conn)
        return None
    else:
        with sqlite3.connect(settings.DB_FILE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("select value from data where key = ?", (key,))
            row = cursor.fetchone()
            return row[0] if row else None

def update_ip(ip):
    insert_or_replace_data("ip", ip)

def get_last_ip():
    return read_data('ip')
