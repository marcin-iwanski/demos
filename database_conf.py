#!/opt/python3/bin/python3
import pymysql
import logs
import sqlanydb

class Database_conf:
	def do_conn_mysql(self,version_dec,is_produccion):
		#is_produccion = 0 > false
		#is_produccion = 1 > true		
		if version_dec == 3:
			pymysql.connect(host='decv3.chlauzwqvh02.sa-east-1.rds.amazonaws.com',user='autentia',password='_voyager.',db='autentia',port=3306)
		elif version_dec == 4 and is_produccion == 0:
			pymysql.connect(host='172.16.14.46',user='dec4',password='_D3c4jTgxB',db='dec4',port=3306)			
		elif version_dec == 4 and is_produccion == 1:
			pymysql.connect(host='172.16.14.70',user='dec4',password='_D3c4jTgxB',db='dec4',port=3307)
		elif version_dec == 2 and is_produccion == 1:
			pymysql.connect(host='base.autentia.cl',user='autentia',password='_voyager.',db='autentia',port=3306)

	def do_conn_iq(self,is_produccion):
		#is_produccion = 0 > false
		#is_produccion = 1 > true
		if is_produccion == 0:
			con = sqlanydb.connect( userid="<user_id>",password="<password>" )
		elif is_produccion == 1:
			con = sqlanydb.connect( userid="<user_id>",password="<password>" )
