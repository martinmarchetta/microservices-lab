from typing import Optional, List, Dict, Any
from app.domain.client_entity import Client

class ClientUseCase:
    def __init__(self):
        from app.repository.client_repository import ClientRepository
        self.client_repository = ClientRepository()

    def get_all_clients(self) -> List[Client]:
        """
        Retrieve all clients from the database
        """
        return self.client_repository.get_all_clients()

    def get_client_by_id(self, client_id: int) -> Optional[Client]:
        """
        Retrieve a client by their ID
        """
        return self.client_repository.get_client_by_id(client_id)

    def create_client(self, client_name: str, client_address: str) -> Client:
        """
        Create a new client with the given details
        """
        return self.client_repository.create_client(client_name=client_name, client_address=client_address)

    def update_client(self, client_id: int, client_data: Dict[str, Any]) -> Optional[Client]:
        """
        Update an existing client's information
        """
        return self.client_repository.update_client(client_id, **client_data)

    def delete_client(self, client_id: int) -> bool:
        """
        Delete a client by their ID
        """
        return self.client_repository.delete_client(client_id)
