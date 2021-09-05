import os
import pymysql
import yaml

from pymysql.err import MySQLError


class SQLClient:
    def __init__(self):
        db_config = self.get_config()
        self._user = db_config["mysql_user"]
        self._password = db_config["mysql_password"]
        self._host = db_config["mysql_host"]
        self._port = 3306
        self._database = db_config["mysql_database"]

    def get_config(self):
        here = os.path.dirname(os.path.realpath(__file__))
        config_file = f"{here}/config/config.yml"

        try:
            with open(config_file, "r") as stream:
                try:
                    config = yaml.load(stream, Loader=yaml.SafeLoader)
                    return config
                except yaml.YAMLError as yerr:
                    print(yerr)
        except FileNotFoundError as ferr:
            print(ferr)

    def get_db_connection(self):
        return pymysql.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            db=self._database,
            port=self._port,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def run_query(self, query, params):
        db = self.get_db_connection()
        try:
            with db.cursor() as cursor:
                cursor.execute(query, params)
                results = cursor.fetchall()
                return results
        except MySQLError as e:
            print("Exception [pymysql.err.{}] {}".format(e.__class__.__name__, e))
            raise e
        finally:
            db.close()

    def run_update(self, query, params):
        db = self.get_db_connection()
        try:
            with db.cursor() as cursor:
                status = cursor.execute(query, params)
                db.commit()
                return status
        except MySQLError as e:
            print("Exception [pymysql.err.{}] {}".format(e.__class__.__name__, e))
            raise e
        finally:
            db.close()
