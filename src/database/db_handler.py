import datetime
from database.db_connect import get_db_connection

CONNECTION = get_db_connection()

def create_snip(s_name: str, s_content: str):
    '''
    Create new snip and return it
    '''
    cur = CONNECTION.cursor()
    sql = """   INSERT INTO Snips (name, content, timestamp) 
                VALUES (:s_name, :s_content, :s_timestamp) """
    inj = {
        "s_name": s_name,
        "s_content": s_content,
        "s_timestamp": datetime.datetime.now()
    }
    lid = cur.execute(sql, inj).lastrowid
    sql = "SELECT * FROM Snips WHERE id=:lid"
    res = cur.execute(sql, {"lid": lid}).fetchone()
    CONNECTION.commit()
    return res

def update_snip(s_id: int, s_name: str, s_content: str):
    '''
    Update by id snip in database
    '''
    try:
        cur = CONNECTION.cursor()
        sql =   """   
                    UPDATE Snips 
                    SET name=:s_name, content=:s_content, timestamp=:s_updated 
                    WHERE id=:s_id 
                """
        inj =   {
                    "s_name": s_name,
                    "s_content": s_content,
                    "s_timestamp": datetime.datetime.now(),
                    "s_id": s_id
                }
        cur.execute(sql, inj)
        CONNECTION.commit()
        return True
    except:
        return False

def load_snips():
    '''
    Return as dict() all snips drom database
    '''
    cur = CONNECTION.cursor()
    sql = "SELECT * FROM Snips"
    snips = cur.execute(sql).fetchall()
    CONNECTION.commit()
    return snips

def create_note(n_name: str, n_content: str):
    '''
    Create note
    '''
    cur = CONNECTION.cursor()
    sql =   """ 
                INSERT INTO Notes (name, content, timestamp) 
                VALUES (:n_name, :n_content, :n_timestamp) 
            """
    inj =   {
                "n_name": n_name,
                "n_content": n_content,
                "n_timestamp": datetime.datetime.now()
            }
    lid = cur.execute(sql, inj).lastrowid
    sql = "SELECT * FROM Notes WHERE id=:lid"
    res = cur.execute(sql, {"lid": lid}).fetchone()
    CONNECTION.commit()
    return res

def update_note(n_id: int, n_name: str, n_content: str):
    '''
    Update note
    '''
    try:
        cur = CONNECTION.cursor()
        sql =   """   
                    UPDATE Notes 
                    SET name=:n_name, content=:n_content, timestamp=:n_timestamp 
                    WHERE id=:n_id
                """
        inj =   {
                    "n_name": n_name,
                    "n_content": n_content,
                    "n_timestamp": datetime.datetime.now(),
                    "n_id": n_id
                }
        cur.execute(sql, inj)
        CONNECTION.commit()
        return True
    except:
        return False

def load_notes():
    '''
    Return as dict() all notes from database
    '''
    cur = CONNECTION.cursor()
    sql = "SELECT * FROM Notes"
    notes = cur.execute(sql).fetchall()
    CONNECTION.commit()
    return notes
