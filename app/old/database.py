import sqlite3 as lite
import sys
import os
import logging


# ========================================
class Database(object):

    PATH2DB = "quadData.db"

    @staticmethod
    def _checkIfTableExists(tablename):
        """Check whether a table exists or not

        Args:
            tablename (TYPE): Table name

        Returns:
            TYPE: Description
        """
        con = lite.connect(Database.PATH2DB)

        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}'".format(tablename))
                if cur.fetchone()[0] == 1:
                    return True
        except lite.Error as e:
            logging.warning("{}".format(e))
        except Exception as e:
            logging.warning("{}".format(e))

        return False

    @staticmethod
    def delete_table(tablename):
        """
        """
        con = lite.connect(Database.PATH2DB)
        try:
            with con:
                # From the connection, we get the cursor object. The cursor is used
                # to traverse the records from the result set. We call the execute()
                # method of the cursor and execute the SQL statement.
                cur = con.cursor()
                cur.execute("DROP TABLE IF EXISTS {}".format(tablename))
                logging.info("Deleting table {}.".format(tablename))
                return True
        except lite.Error as e:
            logging.warning("{}".format(e))
        except Exception as e:
            logging.warning("{}".format(e))
        return False

    @staticmethod
    def create_table(tablename, columnsdict):
        """
        Create table
        columnsdict must be of the form
        columns = {"id": "INT", "name": "TEXT", "price": "INT"}
        """
        columns = ["{} {}".format(key, columnsdict[key]) for key in columnsdict.keys()]

        if not Database._checkIfTableExists(tablename):
            con = lite.connect(Database.PATH2DB)
            try:
                with con:
                    # From the connection, we get the cursor object. The cursor is used
                    # to traverse the records from the result set. We call the execute()
                    # method of the cursor and execute the SQL statement.
                    cur = con.cursor()
                    cur.execute("CREATE TABLE {}({})".format(tablename, ', '.join(columns)))
                    logging.info("New table {} created sucessfully.".format(tablename))
                    return True
            except lite.Error as e:
                logging.warning("{}".format(e))
            except Exception as e:
                logging.warning("{}".format(e))
        else:
            logging.info("Table {} already exists. Reusing...".format(tablename))
        return False

    @staticmethod
    def insertMany(tablename, rows, columnNames=None):
        """
        Insert multiple entries
        db.insertMany("cars", (("Audi", 3000), ("VW", 1000)), columnNames=["name", "price"])
        db.insertMany("cars", ((5, "Hummer2", 3000), (6, "Audi", 4000)))
        """
        if len(rows) == 0:
            logging.info("Nothing to insert!")
            return

        placeholder = ', '.join(len(rows[0]) * ['?'])
        con = lite.connect(Database.PATH2DB)

        try:
            with con:
                cur = con.cursor()
                if isinstance(columnNames, type(None)):
                    cur.executemany("INSERT INTO {} VALUES({})".format(tablename, placeholder), rows)
                elif isinstance(columnNames, list):
                    cur.executemany("INSERT INTO {}({}) VALUES({})".format(tablename, ", ".join(columnNames), placeholder), rows)
                return True
        except lite.Error as e:
            logging.warning("{}".format(e))
        except Exception as e:
            logging.warning("{}".format(e))
        return False


    @staticmethod
    def insertManyInChunks(tablename, rows, columnNames, chunksize=200):
        if len(rows[0])< 999:
            logging.info("This is unnecessary! Use insertMany instead")
            return Database.insertMany(tablename, rows, columns)

        for start in range(0, len(rows[0]), chunksize):
            end = start+chunksize if start+chunksize< len(rows[0]) else len(rows[0])
            subrows = [x[start:end] for x in rows]
            subcolumns = columnNames[start:end]
            Database.insertMany(tablename, subrows, subcolumns)
        return True

    @staticmethod
    def insert(tablename, rows):
        """
        Insert a list of dictionaries
        """
        if len(rows) == 0:
            logging.info("Nothing to insert!")
            return

        con = lite.connect(Database.PATH2DB)

        for row in rows:
            placeholders = ', '.join(['?' for key, val in row.items()])
            vals = [val for key, val in row.items()]
            keys = list(row.keys())
            
            try:
                with con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO {}({}) VALUES({})".format(tablename, ', '.join(keys), placeholders), vals)

            except lite.Error as e:
                logging.warning("{}".format(e))
                return False
            except Exception as e:
                logging.warning("{}".format(e))
                return False

        return True

    @staticmethod
    def update(tablename, row, query):
        """
        Insert a list of dictionaries
        """
        qkeys, qvals = Database._queryProcessor(query)

        vals, keys = [], []
        for key, val in row.items():
            keys.append("{} = ?".format(key))
            vals.append(val)

        con = lite.connect(Database.PATH2DB)
        try:
            with con:
                cur = con.cursor()
                cur.execute("UPDATE {} SET {} WHERE {}".format(tablename, ', '.join(keys), ' AND '.join(qkeys)), vals + qvals)
                return True
        except lite.Error as e:
            logging.warning("{}".format(e))

        except Exception as e:
            logging.warning("{}".format(e))

        return False

    @staticmethod
    def getColumnNames(tablename):
        """
        Get ColumnsNames of DB
        """
        con = lite.connect(Database.PATH2DB)
        try:
            with con:
                con.row_factory = lite.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM {}".format(tablename))
                return cur.fetchone().keys()

        except lite.Error as e:
            logging.warning("{}".format(e))
        except Exception as e:
            logging.warning("{}".format(e))

    @staticmethod
    def _queryProcessor(query):
        vals, keys = [], []
        for key, val in query.items():
            keys.append("({} {} ?)".format(key, val[0]))
            vals.append(val[1])
        return keys, vals

    @staticmethod
    def find(tablename, variables=None, query=None, one=False, distinct=False):
        """Summary

        Args:
            tablename (TYPE): Description
            query (TYPE): Description

        Returns:
            TYPE: Description
        """
        if not query is None:
            keys, vals = Database._queryProcessor(query)
        if variables is None:
            variables = ['*']
        elif not isinstance(variables,list):
            logging.warning("variables must be a list!")
            return
        if distinct:
            distinct = "DISTINCT"
        else:
            distinct = ""

        con = lite.connect(Database.PATH2DB)
        try:
            with con:
                con.row_factory = lite.Row
                cur = con.cursor()
                if not query is None:
                    cur.execute("SELECT {} {} FROM {} WHERE {}".format(distinct, ', '.join(variables), tablename, ' AND '.join(keys)), vals)
                else:
                    cur.execute("SELECT {} {} FROM {}".format(distinct, ', '.join(variables), tablename))

                if one:
                    return dict(cur.fetchone())
                else:
                    return list(map(dict, cur.fetchall()))

        except lite.Error as e:
            logging.warning("{}".format(e))
        except Exception as e:
            logging.warning("{}".format(e))

        return None

    @staticmethod
    def remove(tablename, query):
        """
        Args:
            tablename (TYPE): Description
            query (TYPE): Description
        """
        keys, vals = Database._queryProcessor(query)

        con = lite.connect(Database.PATH2DB)
        try:
            with con:
                cur = con.cursor()
                cur.execute("DELETE FROM {} WHERE {}".format(tablename, ' AND '.join(keys)), vals)
                return True
        except lite.Error as e:
            logging.warning("{}".format(e))
        except Exception as e:
            logging.warning("{}".format(e))
        return False

    @staticmethod
    def getMetaData(tablename):
        """
        Args:
            tablename (TYPE): Description

        Returns:
            TYPE: Description
        """

        con = lite.connect(Database.PATH2DB)
        try:
            with con:

                cur = con.cursor()
                cur.execute("PRAGMA table_info({})".format(tablename))
                return cur.fetchall()

        except lite.Error as e:
            logging.warning("{}".format(e))
        except Exception as e:
            logging.warning("{}".format(e))


# if __name__ == "__main__":

#     columns = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", "name": "TEXT", "price": "INT"}

#     # db.delete_table("cars")
#     Database.create_table("cars", columns)

#     Database.insert("cars", [{"name": "Seat123", "price": 300},
#                              {"name": "VW", "price": 600},
#                              {"name": "Skoda", "price": 10000},
#                              {"name": "Porsche", "price": 600}])

#     #Database.remove("cars", query={"name": ["=", "Audi"], "price": ["<=", 3000]})

#     rows = Database.find("cars", query={"name": ["=", "Audi"], "price": ["<=", 3000]}, one=True)
#     print(rows)

#     rows = Database.find("cars")

#     print(rows)