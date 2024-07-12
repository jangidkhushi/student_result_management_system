import sqlite3

def create_db():
    con = sqlite3.connect(database="equinox.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duration TEXT, charges TEXT,faculty TEXT,exam TEXT, description TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, gender TEXT,dob TEXT,contact TEXT,admission TEXT,course TEXT,state TEXT,city TEXT, pin TEXT,address TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS exam(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,of_marks TEXT, start_date TEXT,end_date TEXT, syllabus TEXT )")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll TEXT, name TEXT,course TEXT, marks_ob TEXT,marks_total TEXT,percentage TEXT)")
    con.commit()
    con.close()

create_db()    



