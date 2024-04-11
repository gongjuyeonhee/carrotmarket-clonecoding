from fastapi import FastAPI, UploadFile, Form, Response,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException #유효하지 않는 계정에 대한 처리
from typing import Annotated
import sqlite3

con = sqlite3.connect('market.db', check_same_thread=False)
cur = con.cursor()


cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                image BLOB,
                price INTEGER NOT NULL,
                description TEXT,
                place TEXT NOT NULL,
                insertAt INTEGER NOT NULL
            );
            """)

app = FastAPI()

SERCRET = "super-coding"
manager = LoginManager(SERCRET, './login')

@manager.user_loader()
def query_user(data):
    WHERE_STATMENTS = f'''id="{data}"'''
    if type(data) == dict:
        WHERE_STATMENTS = f'''id="{data['id']}"'''
    con.row_factory = sqlite3.Row #컬럼명도 가져오는 코드
    cur = con.cursor() #여기 커서 왜 업데이트 해주는 거임?
    user = cur.execute(f"""
                        SELECT * from users WHERE {WHERE_STATMENTS}
                        """).fetchone()
    return user

@app.post('/login')
def login(id:Annotated[str,Form()], 
           password:Annotated[str,Form()]):
    user = query_user(id)
    if not user: #유저가 존재 하나 안존재하나
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(data={
        'sub':{
        'id':user['id'],
        'name':user['name'],
        'email':user['email']
        }
    })
    return {'access_token':access_token}


@app.post('/signup')
def signup(id:Annotated[str,Form()], 
           password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    cur.execute(f"""
                INSERT INTO users(id, name, email, password)
                VALUES ('{id}','{name}','{email}','{password}')
                """)
    con.commit()
    print(id, password)
    return '200'

@app.post('/items')
async def create_item(image:UploadFile, 
                title:Annotated[str,Form()],
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()], 
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]
    ):
    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO items(title, image, price, description, place, insertAt)
                VALUES('{title}', '{image_bytes.hex()}', {price}, '{description}', '{place}', {insertAt})
                """)
    con.commit()
    return '200'

@app.get('/items')
async def get_items(user=Depends(manager)): #로그인 유지되게. 즉 유저로그인 유저되도록
    #컬럼명도 같이 가져옴. 
    con.row_factory =  sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"""
                        SELECT *from items;
                        """).fetchall()
    return JSONResponse(jsonable_encoder(
        dict(row) for row in rows))


@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute(f"""
                            SELECT image from items WHERE id={item_id}
                            """).fetchone()[0]
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')
    



app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")