from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

orders = []

class Order(BaseModel):
    items: List[dict]
    total: float

@app.post('/orders')
def create_order(order: Order):
    order_id = len(orders) + 1
    order_data = {'order_id': order_id, 'items': order.items, 'total': order.total}
    orders.append(order_data)
    return {"message": "Order created", "order_id": order_id}

@app.get('/orders/{order_id}')
def get_order(order_id: int):
    order = next((order for order in orders if order['order_id'] == order_id), None)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="Order not found")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5003)