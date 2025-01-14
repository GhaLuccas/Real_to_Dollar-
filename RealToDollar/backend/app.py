from fastapi import FastAPI

main = FastAPI()


@main.get('/')
def hello():
    return {'message': 'Hello word'}
