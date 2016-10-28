import pymysql

localhost = "198.71.225.61"
username = "ford_umd"
password = "123456789"
database = "Ford_UMD_DataCollection"
db = pymysql.connect(localhost, username, password, database)
cursor = db.cursor()

# execute SQL query using execute() method.
sql = "SELECT vehicleData FROM qianyiw1"
try:
   # Execute the SQL command
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
   	s = str(row).split(' ')
   	for ss in s:
   		if "vehicle_speed" in ss:
   			print ss
   # row = cursor.fetchone()
   # while row is not None:
   # 	print str(row).split()
   # 	row = cursor.fetchone()	
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()
