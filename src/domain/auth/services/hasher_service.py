from typing import Protocol
from abc import abstractmethod


class HasherService(Protocol):
   
    @abstractmethod
    def hash_password(
            self,
            plain_password: str, 
            ) -> str:
        ...
        
    @abstractmethod
    def verify_password(
            self,
            plain_password: str, 
            hashed_password: str
            ) -> bool:
        ...