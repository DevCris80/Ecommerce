from pydantic import BaseModel

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Generic Messages 
class Message(BaseModel):
    message: str