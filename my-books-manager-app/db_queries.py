import sqlite3

DB_PATH = './data.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
FINISHED = 'Finished'

def add_book_to_list(authors, title):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into books(authors, title, status) values(?,?, ?)', (authors, title, NOTSTARTED))
        conn.commit()
        return {"authors": authors, "title": title, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_books():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from books')
        rows = c.fetchall()
        return { "count": len(rows), "books": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_book_status_by_id(id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select status from books where id='%s'" % id)
        status = c.fetchone()[0]
        print(status)
        return status
    except Exception as e:
        print('Error: ', e)
        return None

def update_book_status(id, status):
    #Check if the passed status is a valid value
    if(status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif(status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif(status.lower().strip() == 'finished'):
        status = FINISHED
    else:
        print("Invalid status - " + status)
        return None

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update books set status=? where id=?', (status, id))
        conn.commit()
        return {id: status}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_book(id):
    if get_book_status_by_id(id) is None:
        return {'book id not found': id}
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from books where id=?', (id,))
        conn.commit()
        return {'deleted': id}
    except Exception as e:
        print('Error: ', e)
        return None
