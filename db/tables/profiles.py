from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from sqlmodel import JSON, Column, Field, SQLModel


class ProfileBase(SQLModel):
    username: str = Field(default=None, nullable=True)
    mail: str = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=True)
    sex: str = Field(default=None, nullable=True)
    birthday: datetime = Field(default=None, nullable=True)
    blood_group: str = Field(default=None, nullable=True)
    address: str = Field(default=None, nullable=True)
    job: str = Field(default=None, nullable=True)
    company: str = Field(default=None, nullable=True)


class Profile(ProfileBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    
    __tablename__ = "profiles"
    
    