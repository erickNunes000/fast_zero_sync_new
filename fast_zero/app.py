from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'hello world...'}


@app.get('/users')
def read_users():
    return 'users'
