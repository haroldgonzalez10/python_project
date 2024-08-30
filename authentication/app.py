#Importando librerías
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Inicializando el microservicio
app = FastAPI()

#Data de prueba para testear el microservicio
users = {'harold': {'password': '123', 'email': 'harold@gmail.com'}}

#Modelo de datos que sirve como interfaz de comunicación entre un usuario y un microservicio
class User(BaseModel):
    username: str
    password: str
    email: str = None

#endpoints
@app.post('/login')
def login(user: User):
    if users.get(user.username) and users[user.username]['password'] == user.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post('/register')
def register(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")

    users[user.username] = {'password': user.password, 'email': user.email}
    return {"message": "User registered successfully"}

#código para ejecutar microservicio
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)