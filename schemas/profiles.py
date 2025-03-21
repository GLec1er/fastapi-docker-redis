from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ProfileRead(BaseModel):
    id: UUID
    username: str | None
    mail: str | None
    name: str | None
    sex: str | None
    birthday: datetime | None
    blood_group: str | None
    address: str | None


class ProfileCreate(BaseModel):
    username: str
    mail: str
    name: str
    sex: str
    blood_group: str
