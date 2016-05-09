#!/opt/python3/bin/python3
import time
import datetime

class Archivos:
	def create_file_sql(self,params,nombre_archivo):
		var_fecha = datetime.date.today( )
		var_nombre_archivo = 'sql_files/'+str(var_fecha)+'_'+str(nombre_archivo)+'.sql'
		archivo = open(var_nombre_archivo,'a+')
		archivo.write(params+'\n')
