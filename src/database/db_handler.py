import datetime
from database.db_connect import get_db_connection

connection = get_db_connection()

def init_snippet(content:str):
    cur = connection.cursor()
    sql = "insert into snippets (snippet, created) values (:content, :created)"
    lid = cur.execute(sql, {"content": content, "created": datetime.datetime.now()}).lastrowid
    sql = "select * from snippets where id=:lid"
    res = cur.execute(sql, {"lid": lid}).fetchone()
    connection.commit()
    return res

def load_snippets():
    cur = connection.cursor()
    sql = "select * from snippets"
    res = cur.execute(sql).fetchall()
    connection.commit()
    for item in res:
        yield { "id":       item['id'], 
                "snippet":  item['snippet'], 
                "created":  item['created']
                }


