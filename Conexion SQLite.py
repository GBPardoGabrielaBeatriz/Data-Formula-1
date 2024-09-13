
import sqlitecloud


SQLiteCloud_connectionstring= "sqlitecloud://cqzdwoclsz.sqlite.cloud:8860?apikey=8ZBRx9VjOUr3L8r7arbcH8X27UpFfHwvq7qiaULwWdE"
conn = sqlitecloud.connect(SQLiteCloud_connectionstring)

cursor = conn.execute("USE DATABASE Formula1.db")
cursor = conn.execute("SELECT * FROM DRIVERS")


result = cursor.fetchall()
print(result)

