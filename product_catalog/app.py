#Importando librerías
from fastapi import FastAPI, HTTPException
from typing import List

#Inicializando el microservicio
app = FastAPI()

#Data de prueba para testear el microservicio
products = [
    {'id': 1, 'name': 'Portatil', 'price': 1500},
    {'id': 2, 'name': 'Celular', 'price': 800},
    {'id': 3, 'name': 'Diadema', 'price': 200},
    {'id': 4, 'name': 'Teclado', 'price': 100},
    {'id': 4, 'name': 'Escritorio', 'price': 3000}
]

#endpoints
@app.get('/products', response_model=List[dict])
def get_products():
    return products

@app.get('/products/{product_id}', response_model=dict)
def get_product(product_id: int):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

#código para ejecutar microservicio
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)