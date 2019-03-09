#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
from flask import *
import warnings
warnings.filterwarnings("ignore")
import MySQLdb
import MySQLdb.cursors
from config import *

# 改动处，省略掉前面的MYSQLdb和cursors
import pymysql

app = Flask(__name__)
app.config.from_object(__name__)

# 连接数据库
def connectdb():
	db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass = MySQLdb.cursors.DictCursor)
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

def connectdb
	db = pymysql.connect(host=HOST, user=USER, passwd=PASSWORD',
                       db=DATABASE, port=PORT, charset=CHAREST,cursorclass=pymysql.cursors.DictCursor)
	cursor = db.cursor()  # 光标对象
	db.autocommit(True)
        return (db,cursor)


# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()

# 首页
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
