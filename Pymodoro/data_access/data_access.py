#! /usr/bin/python

import sqlite3


class DataAccess:

    def __init__(self, db_filename):
        self.db_filename = db_filename

    def get_connection(self):
        conn = sqlite3.connect(self.db_filename)
        return conn

    def add_new_user(self, user, email):
        conn = self.get_connection()
        c = conn.cursor()
        new_user_id = self.get_max_user_id()+1
        sql_statement = "insert into Users values(?,?,?)"
        c.execute(sql_statement, (new_user_id, user, email))
        conn.commit()
        conn.close()

    def get_max_user_id(self):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("select max(User_ID) from Users")
        result = c.fetchone()
        conn.close()

        if result[0] is not None:
            return result
        else:
            return 0
