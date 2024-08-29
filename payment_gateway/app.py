from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    order_id: int
    payment_method: str
    amount: float

@app.post('/payment')
def process_payment(payment: Payment):
    return {"message": f"Payment of {payment.amount} using {payment.payment_method} for order {payment.order_id} processed successfully"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5004)
