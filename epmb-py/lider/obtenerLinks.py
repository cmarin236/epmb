import dryscrape
import unicodedata
import MySQLdb
from bs4 import BeautifulSoup

DB_HOST = raw_input("Servidor   : ")
DB_USER = raw_input("Usuario    : ")
DB_PASS = raw_input("Password   : ")
DB_NAME = raw_input("Base Datos : ")
DB_TABLA= raw_input("Tabla      : ")

def run_query(query=''):
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

	conn = MySQLdb.connect(*datos) 	# Conectar a la base de datos
	cursor = conn.cursor()			# Crear un cursor
	cursor.execute(query)			# Ejecutar una consulta

	if query.upper().startswith('SELECT'):
		data = cursor.fetchall()	# Traer los resultados de un select
	else:
		conn.commit()				# Hacer efectiva la escritura de datos
		data = None

	cursor.close()					# Cerrar el cursor
	conn.close()					# Cerrar la conexion

	return data


query = "SELECT * FROM " + DB_TABLA
result = run_query(query) 
# print result


for registro in run_query(query):
	print (registro[0])