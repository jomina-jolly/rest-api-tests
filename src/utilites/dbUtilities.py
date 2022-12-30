import pymysql
from src.utilites.credentialUtilities import CredentialUtilites
from src.configs.hosts_config import DB_DETAILS
import logging as logger

class DBUtilities():

    
    def __init__(self) -> None:
        db_credentials = CredentialUtilites.get_db_credentials()
        self.db_username = db_credentials['db_user']
        self.db_password = db_credentials['db_password']

    def create_connection(self):
        connection = pymysql.connect(host=DB_DETAILS['HOST'], user=self.db_username, password=self.db_password, port=DB_DETAILS['PORT'])
        return connection

    def execute_sql(self, sql):
        logger.debug(f"Running query: {sql}")

    def execute_select(self, sql):
        logger.debug(f"Running query: {sql}")

        cnx = self.create_connection()
        
        try:
            cur = cnx.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            resp_dic = cur.fetchall()
            cur.close()

        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n \
                Error: {str(e)} ")
        finally:
            cnx.close()
        return resp_dic