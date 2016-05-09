#!/opt/python3/bin/python3
from logs import Logs
import pymysql
from archivos import Archivos
from config import Config
import time
import datetime
import sys
import pymysql.cursors

def get_doctos_dec(self):

	config = Config()
	logs = Logs()
	archivo = Archivos()
	hoy = datetime.date.today( )
	ayer = hoy - datetime.timedelta(days=1)
	is_biometria = 0
	is_firma_tipo = ''
	#
	logs.escribe_log('Abriendo conexion a ddbb: '+str(config.IP_HOST_DEC3_PROD))
	#
	db_conn = pymysql.connect(
		host=str(config.IP_HOST_DEC3_PROD),
		user=str(config.USER_DB_DEC3_PROD),
		password=str(config.PASS_DB_DEC3_PROD),
		db=str(config.DDBB_DB_DEC3_PROD),
		port=int(config.PORT_DB_DEC3_PROD))
	sql_escape = db_conn.escape_string
	cursor = db_conn.cursor(pymysql.cursors.DictCursor)
	# ocupar parametrizacion en execute segun reglas de DBAPI
	sql = """
	SELECT
		a.Descripcion AS nombre,
		a.Codigo AS nro_docto, 
		f.FechaFirma AS fecha_firma, 
		f.Rut AS rut, 
		f.NroAudit AS naudit, 
		f.RolFirmante AS rol_firmante, 
		a.Institucion AS institucion
	FROM
		DArchivos AS a,
		DFirmantes AS f
	WHERE
		a.Codigo = f.CodigoArchivo
		AND a.FechaCreacion between %(ayer)s AND %(hoy)s
		AND a.Institucion = 'AUTENTIA'";"""
	try:
		cursor.execute(sql, {"ayer": ayer, "hoy": hoy})
		db_conn.commit()
		logs.escribe_log('Ejecutando query: '+sql)
		results = cursor.fetchall() # ocupar fetchmany
		for row in results:
			#Codigo = row[0]
			#Nombre = row[1]
			#FechaCreacion: = row[2]
			#FechaModificacion: = row[3]
			#Reemplazable: = row[4]
			#Visible: = row[5]
			#Descripcion: = row[6]
			#CodigoPadre: = row[7]
			#Metadata: = row[8]
			#Rut: = row[9]
			#Institucion: = row[10]
			#Sistema: = row[11]
			#GenPdf: = row[12]
			#CodLugar: = row[13]
			nombre = row['nombre']
			nro_docto  = row['nro_docto']
			fecha_firma = row['fecha_firma']
			rut = row['rut']
			naudit = row['naudit']
			rol_firmante = row['rol_firmante']
			institucion = row['institucion']
			#
			is_firma_tipo = naudit[:4]
			if (is_firma_tipo == 'NONE'):
				is_biometria = 1
			else:
				is_biometria = 0
			#Crear archivo sql al IQ
			var_insert = "insert into DEC_FirmadosIQ values ('', '"+str(institucion)+"','"+str(nro_docto)+"','"+str(nombre)+"','NA','"+str(fecha_firma)+"','"+str(rol_firmante)+"','"+str(rut)+"','"+str(naudit)+"',3,"+int(is_firma_tipo)+");"
			var_insert = "insert into DEC_FirmadosIQ values ('', %(institucion)s, %(nro_docto)s, %(nombre)s, 'NA', %(fecha_firma)s, %(rol_firmante)s, %(rut)s, %(naudit)s, 3, %(is_firma_tipo)s);" % (
				dict(	institucion=sql_escape(institucion),
					nro_docto=sql_escape(nro_docto),
					nombre=sql_escape(nombre),
					fecha_firma=sql_escape(fecha_firma),
					rol_firmante=sql_escape(rol_firmante),
					rut=sql_escape(rut),
					naudit=sql_escape(naudit),
					is_firma_tipo=sql_escape(is_firma_tipo),
				))
			archivo.create_file_sql(var_insert,'DArchivos')
		logs.escribe_log('fin proceso ddbb DEC3')
		logs.escribe_log('Inicio proceso ddbb DEC4')
		#self.get_doctos_dec4()
	except:
		logs.escribe_log('Imposible Ejecutar query DArchivos '+str(sys.exc_info()))
		raise

def get_doctos_dec4(self):
	config = Config()
	logs = Logs()
	archivo = Archivos()
	#is_produccion: 0 => TRUE
	#is_produccion: 1 => FALSE
	is_biometria = 0
	#
	ip_ddbb = ''
	ddbb = ''
	user_ddbb = ''
	pass_ddbb = ''
	port_ddbb = ''
	#
	is_produccion = config.PRODUCCION
	#
	if (is_produccion == 0):
		ip_ddbb = config.IP_HOST_DEC4_PROD
		ddbb = config.DDBB_DB_DEC4_PROD
		user_ddbb = config.USER_DB_DEC4_PROD
		pass_ddbb = config.PASS_DB_DEC4_PROD
		port_ddbb = 3307
	else:
		ip_ddbb = config.IP_HOST_DEC4_PROD
		ddbb = config.DDBB_DB_DEC4_PROD
		user_ddbb = config.USER_DB_DEC4_PROD
		pass_ddbb = config.PASS_DB_DEC4_PROD
		port_ddbb = 3306
	#
	logs.escribe_log('Abriendo conexion a ddbb: '+str(ip_ddbb))
	#
	db_conn = pymysql.connect(host=str(ip_ddbb),user=str(user_ddbb),password=str(pass_ddbb),db=str(ddbb),port=int(port_ddbb))
	cursor = db_conn.cursor()
	#
	hoy = datetime.date.today( )
	ayer = hoy - datetime.timedelta(days=1)
	try:
		logs.escribe_log('Ejecutando query: '+sql)
		cursor.execute("""\
			select *
			from dc4_Documento
			where Institucion = %(Institucion)s""", dict(
				Institucion=institucion,
			))
		cursor.execute("""\
			select *
			from dc4_Documento
			where Institucion = ?""", (institucion,))
		db_conn.commit()
		results = cursor.fetchall()
		for row in results:
			nombre = row[0]
			fecha_firma = row[2]
			rut = row[3]
			naudit = row[4]
			rol_firmante = row[5]
			#
			is_firma_tipo = naudit[:4]
			if (is_biometria == 'NONE'):
				is_biometria = 1
			else:
				is_biometria = 0
			#Crear archivo sql al IQ
			var_insert = "insert into DEC_FirmadosIQ values ('','"+str(institucion)+"','"+str(nombre)+"','TIPODOCTO','"+str(fecha_firma)+"','"+str(rol_firmante)+"','"+str(rut)+"','"+naudit+"',4,'"+is_firma_tipo+"');"
			archivo.create_file_sql(var_insert,'dc4_Documento')
	except:
		logs.escribe_log('Imposible Ejecutar query dc4_Documento')
