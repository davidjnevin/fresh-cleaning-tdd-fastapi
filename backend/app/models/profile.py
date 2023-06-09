from typing import Optional

from app.models.core import CoreModel, DateTimeModelMixin, IDModelMixin
from pydantic import EmailStr, HttpUrl


class ProfileBase(CoreModel):
    full_name: Optional[str]
    phone_number: Optional[str]
    bio: Optional[str]
    image: Optional[HttpUrl]


class ProfileCreate(ProfileBase):
    """
    The only field required to create a profile is a user id
    """

    user_id: int


class ProfileUpdate(ProfileBase):
    """
    Allow users to update any or no fields, except user_id
    """

    pass


class ProfileInDB(IDModelMixin, DateTimeModelMixin, ProfileBase):
    user_id: int
    username: Optional[str]
    email: Optional[EmailStr]


class ProfilePublic(ProfileInDB):
    pass
