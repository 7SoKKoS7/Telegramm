import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('client_base.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS client_base(id INTEGER PRIMARY KEY AUTOINCREMENT, client_id_telega INTEGER'
                 ', message_client TEXT, date_msg TEXT)')
    base.commit()


