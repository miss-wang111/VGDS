import os

DIALECT = 'mysql'
DRIVER = 'mysqldb'
# 本地的数据库
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'liverdb'
# 服务器上的数据库
# USERNAME = 'root'
# PASSWORD = 'BIT@bio#123'
# HOST = 'bit.zust.edu.cn'
# PORT = '3307'
# DATABASE = 'liverdb'

#最终数据库
# USERNAME = 'root'
# PASSWORD = '123456'
# HOST = 'bit.zust.edu.cn'
# PORT = '6904'
# DATABASE = 'liverdb'

DB_URL = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(24)
