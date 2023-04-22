from fastapi import FastAPI
import uvicorn


app=FastAPI()

@app.get('/')
def get_title():
    return 'Welcome to My API'
