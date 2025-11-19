import pymysql

def conn():
    conexion = pymysql.connect(
        host='200.58.106.156',
        user='c2710325_killer',
        passwd='SistemaIES6021',
        database='c2710325_admin'
    )
    print('Conexion Exitosa')
    return conexion
