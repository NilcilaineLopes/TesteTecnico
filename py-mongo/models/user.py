from distutils.command.upload import upload
from pydantic import BaseModel

class User(BaseModel):
    name : str
    email: str
    phone: str
    profession: str
    cit: str
    district: str
    Street: str
    numberHouse: str
    zipcode: str
