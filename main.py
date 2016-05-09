#!/opt/python3/bin/python3
from notificaciones import Notificaciones
from query import Query
from logs import Logs

class Inicio:

	def init_prog(self):
		#Intanciar class logs
		logs = Logs()
		#Intanciar class notificaciones
		notificaciones = Notificaciones()
		#Intanciar class query
		sql_q = Query()
		#Inicio del programa
		logs.escribe_log('INICIO programa')
		#Obteniendo documentos a dec3
		logs.escribe_log('Obteniendo documentos dec3')
		sql_q.get_doctos_dec()
		logs.escribe_log('FIN programa')

#Inicio del programa
init_progama = Inicio()
init_progama.init_prog()
