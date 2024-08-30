#Importando librerías
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

#Inicializando el microservicio
app = FastAPI()

#Data de prueba para testear el microservicio
cart = {}

#Modelo de datos que sirve como interfaz de comunicación entre un usuario y un microservicio
class CartItem(BaseModel):
    product_id: int
    quantity: int

#endpoints
@app.get('/cart', response_model=Dict[int, int])
def get_cart():
    return cart

@app.post('/cart')
def add_to_cart(item: CartItem):
    if item.product_id in cart:
        cart[item.product_id] += item.quantity
    else:
        cart[item.product_id] = item.quantity
    return {"message": "Item added to cart"}

@app.delete('/cart')
def remove_from_cart(item: CartItem):
    if item.product_id in cart:
        del cart[item.product_id]
        return {"message": "Item removed from cart"}
    else:
        raise HTTPException(status_code=404, detail="Item not found in cart")

#código para ejecutar microservicio
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5002)