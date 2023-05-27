from pydantic import BaseModel


class baseSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    required: str

