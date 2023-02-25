from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
    email: str
class Token(BaseModel):
    access_token: str
    token_type: str