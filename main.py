#!/opt/python3/bin/python3

from notificaciones import Notificaciones
import query
from logs import Logs

def main():
	#Intanciar class logs
	logs = Logs()
	#Intanciar class notificaciones
	notificaciones = Notificaciones()
	#Intanciar class query
	#Inicio del programa
	logs.escribe_log('INICIO programa')
	#Obteniendo documentos a dec3
	logs.escribe_log('Obteniendo documentos dec3')
	query.get_doctos_dec()
	logs.escribe_log('FIN programa')


main()
