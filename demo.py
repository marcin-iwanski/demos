#!/opt/python3/bin/python3
import time
import datetime
hoy = datetime.date.today( )
ayer = hoy - datetime.timedelta(days=1)
print(hoy, ayer)
