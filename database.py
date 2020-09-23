import sqlite3

__connection=None

def get_connection():
    global __connection
    if __connection is None:
        __connection=sqlite3.connect("database.db")
    return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS events')
        c.execute('''
            CREATE TABLE IF NOT EXISTS events (
              event_date     DATE,
              event          TEXT
            )
        ''')
    conn.commit()

def add_event(event_date:date, event:text):
    conn=get_connection()
    c=conn.cursor()
    c.execute('INSERT INTO events(event_date,event) VALUES (?,?)',(event_date,event))
    conn.commit()

#if __name__ == '__main__':
 #   init_db()
  #  add_event(event_date='2020-04-05',event='Birthday')




