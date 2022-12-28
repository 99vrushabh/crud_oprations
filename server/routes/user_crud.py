from fastapi import APIRouter, status, HTTPException
from server.utils.database import SessionLocal
from server.models.user import payment
from server.models.user import Client

router = APIRouter()
db = SessionLocal()


@router.get('/users', status_code=200)
def get_all_users():
    clients = db.query(Client).all()

    return {"data": clients, "status": 200, "message": "data get successfully"}


@router.get('/users/{user_id}', status_code=status.HTTP_200_OK)
def get_an_user(user_id: int):
    client = db.query(Client).filter(Client.id == user_id).first()

    return {"data": client, "status": 200, "message": "data retrive successfully"}


@router.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(payment: payment):

    db_client = db.query(Client).filter(Client.id == payment.id).first()

    if db_client is not None:
        raise HTTPException(status_code=400, detail="data already exists")

    new_client = Client(
        id=payment.id,
        name=payment.name,
        status=payment.status,
        date_birth=payment.date_birth
    )

    db.add(new_client)
    db.commit()

    return {"status": 200, "message": "data post successfully"}


@router.put('/users/{user_id}', status_code=status.HTTP_200_OK)
def update_an_user(user_id: int, client: payment):

    client_to_update = db.query(Client).filter(Client.id == user_id).first()
    client_to_update.id = client.id
    client_to_update.name = client.name
    client_to_update.status = client.status
    client_to_update.date_birth = client.date_birth
 
    db.commit()

    return {"status": 200, "message": "user updated successfully"}


@router.delete('/users/{user_id}')
def delete_user(user_id: int):
    client_to_delete = db.query(Client).filter(Client.id == user_id).first()

    if client_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

    db.delete(client_to_delete)
    db.commit()

    return {"data": client_to_delete, "status": 200, "message": "user delete successfully"}
