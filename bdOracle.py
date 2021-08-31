import cx_Oracle


con = cx_Oracle.connect(
	user = "pcprogramer",
	password = "pc12345",
	dsn = "localhost/xe")

print('Sucesso')


try:
	cur = con.cursor()
	cur.execute('select * from Taluno')
	rows = cur.fetchone()
	print(rows)

except:
	print('erro de consulta')


