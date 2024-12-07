from flask import Flask, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
import db as dbase
from product import Product

# Instanciar la conexión a la BBDD
db = dbase.dbConnection()

app = Flask(__name__)

# Secret Key
app.secret_key = 'secret_key'


# Ruta Principal
@app.route('/')
def index():
    products = db['products']
    data = products.find()
    return render_template('index.html', dataProducts = data)


# Ruta Agregar Productor
@app.route('/add_product', methods =['POST'])
def add_product():
    if request.method == 'POST':
        products = db['products']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        if nombre and precio and cantidad:
            product = Product(nombre, precio, cantidad)
            products.insert_one(product.toDBCollection())
            flash("Producto agregado correctamente!")
            return redirect(url_for('index'))


# Ruta Editar Producto
@app.route('/edith_product/<id>')
def edith_product(id):
    products = db['products']
    data = products.find_one( { "_id": ObjectId(id) } )
    return render_template('edith_product.html', dataProduct = data)


@app.route('/update_product/<id>', methods=['POST'])
def update_product(id):
    if request.method == 'POST':
        products = db['products']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        products.update_one(
            { '_id': ObjectId(id) },
            {
                '$set':{
                    'nombre': str(nombre),
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                }
            }
        )
        flash("Producto actualizado correctamente!")
        return redirect(url_for('index'))


# Ruta Eliminar Producto
@app.route('/delete_product/<string:id>')
def delete_product(id):
    products = db['products']
    products.delete_one( { '_id': ObjectId(id) } )
    flash("Producto eliminado correctamente!")
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(port=4000, debug=True)