import pymysql

def conn():
    conexion = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='ies6021'
    )
    print('Conexion Exitosa')
    return conexion