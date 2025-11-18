#-------------------- SECCION DE IMPORTACION DE MODULOS ----------------------------------
from flask import Flask,render_template,redirect,url_for,request,flash
from db import conn 

#-------------------- SECCION CREACION DE API -------------------------------------------

app = Flask(__name__)

#-------------------- SECCION RUTA PRINCIPAL -------------------------------------------

@app.route("/")
def home():
    return render_template("/sitio/index.html")

#--------------------- SECCION LIBROS ---------------------------------------------------

#Ruta Libros
@app.route("/libros")
def libros():
    return render_template('/sitio/libros.html')
#-------------------- SECCION ALUMNOS -------------------------------------------

#Ruta de alumnos
@app.route("/alumno",methods=['GET'])
def alumno():
    query = 'select * from alumno'
    conexion = conn()
    cursor = conexion.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template("/sitio/alumnos.html",alumno=data)

 #Ruta para guardar Alumnos
@app.route("/reg_alumno",methods=['POST'])
def reg_alumnos():
    conexion = conn()
    query = 'INSERT INTO alumno(apenomb,dni,correo)VALUES(%s,%s,%s)'
    
    nombre = request.form['nombre']
    dni = request.form['dni']
    correo = request.form['correo']
    cursor = conexion.cursor()
    cursor.execute(query,(nombre,dni,correo))
    conexion.commit()
    print("Registro Guardado Exitosamente")
    return redirect(url_for('alumno'))

#Eliminar alumno
@app.route("/delete/<string:id>")
def delete_Alumno(id):
    query = "delete from alumno where idalumno = %s"
    conexion = conn()
    cursor = conexion.cursor()
    cursor.execute(query,(id))
    conexion.commit()
    return redirect(url_for('alumno'))
#-------------------- SECCION ALUMNOS -------------------------------------------
#Actualizar ALumnos
@app.route("/Update_Alumno/<string:id>",methods=['POST'])
def Actualizar_Alumno(id):
    conexion = conn()
    nombre = request.form['name']
    dni = request.form['document']
    correo = request.form['email']
    query = 'UPDATE alumno SET apenomb = %s,dni=%s,correo=%s WHERE idalumno = %s'
    cursor = conexion.cursor()
    cursor.execute(query,(nombre,dni,correo,id))
    conexion.commit()
    return redirect(url_for('alumno'))

#-------------------- SECCION CARRERAS ------------------------------------------
#ruta Carreras
@app.route("/carrera",methods=['GET'])
def carrera():
    return render_template("/sitio/carreras.html")

# -------------------- SECCION DOCENTES -----------------------------------------

#Ruta para Docentes

@app.route("/Docentes")
def homeDocentes():
    query = 'select * from docente'
    conexion = conn()
    cursor = conexion.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template("/sitio/docentes.html",docente=data)

 #Ruta para guardar Docentes
@app.route("/reg_docente",methods=['POST'])
def reg_docente():
    conexion = conn()
    query = 'INSERT INTO docente(apenomb,dni,correo)VALUES(%s,%s,%s)'
    
    nombre = request.form['nombre']
    dni = request.form['dni']
    correo = request.form['correo']
    cursor = conexion.cursor()
    cursor.execute(query,(nombre,dni,correo))
    conexion.commit()
    print("Registro Guardado Exitosamente")
    return redirect(url_for('homeDocentes'))

#Eliminar Docentes
@app.route("/delete_doc/<string:id>")
def delete_Docente(id):
    query = "delete from docente where iddocente = %s"
    conexion = conn()
    cursor = conexion.cursor()
    cursor.execute(query,(id))
    conexion.commit()
    return redirect(url_for('homeDocentes'))

#-------------------- SECCION ARRANQUE SERVIDOR FLASK ----------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4700, debug=True)



