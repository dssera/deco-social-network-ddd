import bcrypt

from domain.auth.services.hasher_service import HasherService


class HasherServiceImpl(HasherService):

    def hash_password(
            self,
            plain_password: str, 
            ) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(plain_password, salt)
        
    def verify_password(
            self,
            plain_password: str, 
            hashed_password: str
            ) -> bool:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())