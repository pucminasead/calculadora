from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de Calculadora!"}

@app.get("/soma/")
def soma(x: int, y: int):
    return {"soma": x + y}

@app.get("/divisao/")
def soma(x: int, y: int):
    return {"divisão": x / y}

@app.get("/subtracao/")
def soma(x: int, y: int):
    return {"subtração": x - y}
