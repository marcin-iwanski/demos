#!/opt/python3/bin/python3

# no se necesita, ocupar logging directamente

import datetime
import logging

class Logs:
	
	def escribe_log(self,params):
		logging.basicConfig(filename="app_cobros_dec.log", level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
		logging.info(params)
