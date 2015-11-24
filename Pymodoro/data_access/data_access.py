#! /usr/bin/python

import sqlite3


class DataAccess:

    def __init__(self, db_filename):
        self.db_filename = db_filename

    @classmethod
    def get_connection(cls):
        conn = sqlite3.connect(cls.db_filename)
        return conn

    @classmethod
    def add_new_user(cls, user, email):
        conn = cls.get_connection()
        c = conn.cursor()
        new_user_id = cls.get_max_user_id()+1
        sql_statement = "insert into Users values(?,?,?)"
        c.execute(sql_statement, (new_user_id, user, email))
        conn.commit()
        conn.close()

    @classmethod
    def get_max_user_id(cls):
        conn = cls.get_connection()
        c = conn.cursor()
        c.execute("select max(User_ID) from Users")
        result = c.fetchone()
        conn.close()

        if result[0] is not None:
            return result
        else:
            return 0
