

# MSSQL

mssql_db_username = 'fullreport'
mssql_db_password = 'fotbalanalytika2018FR#'
mssql_db_name = 'fullreport'
mssql_db_hostname = 'fullreportserver.database.windows.net,1433'

# mssql_db_username = 'sa'
# mssql_db_password = '11HacksSQL'
# mssql_db_name = '11Hacks'
# mssql_db_hostname = '13.80.131.134,1433'

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "SOME SECRET"


# SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_ADDR}:1433/{DB_NAME}?driver=SQL+Server+Native+Client+11.0".format(DB_USER=mssql_db_username,
#                                                                                         DB_PASS=mssql_db_password,
#                                                                                         DB_ADDR=mssql_db_hostname,
#                                                                                         DB_NAME=mssql_db_name)


SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_ADDR}:1433/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server".format(DB_USER=mssql_db_username,
                                                                                        DB_PASS=mssql_db_password,
                                                                                        DB_ADDR=mssql_db_hostname,
                                                                                        DB_NAME=mssql_db_name)
