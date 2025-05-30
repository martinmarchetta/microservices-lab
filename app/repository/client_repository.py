from sqlalchemy.orm import Session
from app.domain.client_entity import Client
from app.application.container import Container

class ClientRepository:
    def __init__(self):
        self.session = Container.sqlalchemy_db.session

    def get_all_clients(self):
        return self.session.query(Client).all()

    def get_client_by_id(self, client_id: int):
        return self.session.query(Client).filter(Client.id == client_id).first()

    def create_client(self, client_name: str, client_address: str):
        client = Client(client_name=client_name, client_address=client_address)
        self.session.add(client)
        self.session.commit()
        return client

    def update_client(self, client_id: int, **kwargs):
        client = self.get_client_by_id(client_id)
        if not client:
            return None
        for key, value in kwargs.items():
            setattr(client, key, value)
        self.session.commit()
        return client

    def delete_client(self, client_id: int):
        client = self.get_client_by_id(client_id)
        if not client:
            return False
        self.session.delete(client)
        self.session.commit()
        return True
