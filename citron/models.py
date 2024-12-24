from pydantic import BaseModel

class Member(BaseModel):
    id: int
    name: str
    email: str
