import cx_Oracle

connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

cursor = connection.cursor()
try:

    dp = input("Número de departamento:")
    loc = ""

    args = (loc, dp)
    result_args = cursor.callproc('DevolverLocalidad', args)
    print(result_args[0])
    print(result_args[1])




except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()
