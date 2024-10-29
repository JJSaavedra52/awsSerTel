from flask import Blueprint, request, jsonify
from products.models.product_model import Product
from users.models.db import db

product_controller = Blueprint('product_controller', __name__)

# Obtener todos los productos
@product_controller.route('/api/products', methods=['GET'])
def get_products():
    print("listado de productos")
    products = Product.query.all()
    result = [{'ref': product.ref, 'name': product.name, 'price': product.price, 'description': product.description} for product in products]
    return jsonify(result)

# Obtener un producto por referencia
@product_controller.route('/api/products/<string:ref>', methods=['GET'])
def get_product(ref):
    print("obteniendo producto")
    product = Product.query.get_or_404(ref)
    return jsonify({'ref': product.ref, 'name': product.name, 'price': product.price, 'description': product.description})

# Crear un nuevo producto
@product_controller.route('/api/products', methods=['POST'])
def create_product():
    print("creando producto")
    data = request.json
    new_product = Product(ref=data['ref'], name=data['name'], price=data['price'], description=data['description'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Producto creado exitosamente'}), 201

# Actualizar un producto existente
@product_controller.route('/api/products/<string:ref>', methods=['PUT'])
def update_product(ref):
    print("actualizando producto")
    product = Product.query.get_or_404(ref)
    data = request.json
    product.name = data['name']
    product.price = data['price']
    product.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Producto actualizado exitosamente'})

# Eliminar un producto existente
@product_controller.route('/api/products/<string:ref>', methods=['DELETE'])
def delete_product(ref):
    product = Product.query.get_or_404(ref)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Producto eliminado exitosamente'})

