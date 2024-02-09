import  sqlite3


db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS artists(
id INTEGER PRIME KEY INCREMENT,
name TEXT , 
address TEXT , 
town TEXT ,
country TEXT , 
post_code INTENGER
)

''')
def add_datas():
    cursor.execute('''
    INSERT INTO artists(
    name, address, town, country , post_code)
    VALUES(?,?,?,?,?)
     ''', (ati,adresi,qalasi,watani,postcode))
    db.commit() 
cursor.execute('''
CREATE TABLE IF NOT EXISTS arts(
id INTEGER AUTO INCREMENT, 
artist_id INTEGER,
title TEXT,
style TEXT,
price INTEGER
)

''')
     