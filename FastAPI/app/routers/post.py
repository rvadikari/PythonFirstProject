from fastapi import Response,status,HTTPException,Depends,APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import models,schema
from ..database import engine,get_db
from ..oauth2 import get_current_user

router=APIRouter(
    prefix="/posts"
)

@router.get("/",response_model=List[schema.Post])
async def get_posts(db:Session=Depends(get_db),user_id:int = Depends(get_current_user),limit:int=10,skip:int=0): 
    my_posts=db.query(models.Post).order_by(models.Post.id).limit(limit).offset(skip).all()
    return my_posts 


@router.get("/{id}",response_model=schema.Post)
async def get_post(id:int,response:Response, db:Session=Depends(get_db),user_id:int = Depends(get_current_user)): 
    # post=find_post(id)
    post= db.query(models.Post).filter(models.Post.id== id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} is not found")
    return post


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_post(post:schema.PostModel, db: Session=Depends(get_db),
                  current_User:int = Depends(get_current_user)):
    
    new_post=models.Post(user_id=current_User.id,** post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    print(new_post.user)
    return new_post


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),current_user:int = Depends(get_current_user)):
    # index=None
    # for i,p in enumerate(my_posts):
    #     if p["id"]==id:
    #         index=i
    # print(index)
    post= db.query(models.Post).filter(models.Post.id==id)
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"id with {id} is not found in the list")
    if post.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform the requested action")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schema.Post)
def update_post(id:int,updated_post:schema.PostModel, db:Session=Depends(get_db),current_user:int = Depends(get_current_user)):
    # index=None
    # for i,p in enumerate(my_posts):
    #     if p["id"]==id:
    #         index=i
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id with {id} is not found in the list")
    if post.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform the requested action")
    # post_dict=post.dict()
    # post_dict['id']=id
    # my_posts[index]=post_dict
    post.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(post.first())
    return post.first()
