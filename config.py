#!/opt/python3/bin/python3

class Config:
	#Constantes del sistema
	#DEC3
	IP_HOST_DEC3_PROD = 'decv3.chlauzwqvh02.sa-east-1.rds.amazonaws.com'
	USER_DB_DEC3_PROD = 'autentia'
	PASS_DB_DEC3_PROD = '_voyager.'
	DDBB_DB_DEC3_PROD = 'autentia'
	PORT_DB_DEC3_PROD = '3306'
	#DEC4 PROD
	IP_HOST_DEC4_PROD = '172.16.14.70'
	USER_DB_DEC4_PROD = 'dec4'
	PASS_DB_DEC4_PROD = '_D3c4jTgxB'
	DDBB_DB_DEC4_PROD = 'dec4'
	PORT_DB_DEC4_PROD = '3307'
	#DEC4 QA
	IP_HOST_DEC4_QA = '172.16.14.46'
	USER_DB_DEC4_QA = 'dec4'
	PASS_DB_DEC4_QA = '_D3c4jTgxB'
	DDBB_DB_DEC4_QA = 'dec4'
	PORT_DB_DEC4_QA = '3306'
	#CONSTANTE PARA function  get_doctos_dec4 de la clase Query SOLO PARA DEC4
	#PRODUCCION = 0 => True, PRODUCCION = 1 => FALSE, QA
	PRODUCCION = 1
