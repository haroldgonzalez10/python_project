#Importando librerías
from fastapi import FastAPI
from pydantic import BaseModel

#Inicializando el microservicio
app = FastAPI()

#Modelo de datos que sirve como interfaz de comunicación entre un usuario y un microservicio
class Payment(BaseModel):
    order_id: int
    payment_method: str
    amount: float

#endpoints
@app.post('/payment')
def process_payment(payment: Payment):
    return {"message": f"Payment of {payment.amount} using {payment.payment_method} for order {payment.order_id} processed successfully"}

#código para ejecutar microservicio
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5004)