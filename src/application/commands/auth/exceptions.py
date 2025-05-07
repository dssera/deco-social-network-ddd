
class InvalidCredentialsException(Exception):
    pass

class UserDoesntExist(InvalidCredentialsException):
    pass

class InvalidPassword(InvalidCredentialsException):
    pass