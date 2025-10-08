from flask import Flask,render_template,redirect,url_for,request,flash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/sitio/index.html")

#Seccion de Libros
@app.route("/libros")
def libros():
    return render_template("/sitio/libros.html")



if __name__=='__main__':
    app.run(debug=True)


