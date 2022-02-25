
from email import message
from random import randrange
from typing import List
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body



from . import models
from .routers import post,user,auth

from sqlalchemy.orm import Session
from .database import engine,get_db


models.Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)



     


my_posts= [{"title":"post1", "content":"my test content1","published":True,"rating":4,"id":1},
            {"title":"post2", "content":"my test content2","published":True,"rating":3,"id":2},
            {"title":"post3", "content":"my test content3","published":True,"rating":4,"id":3}]

def find_post(id:int):
    for p in my_posts:
        if p['id']== id:
            return p
       

@app.get("/")
async def root(db:Session=Depends(get_db)): 
   return {"root method"}




