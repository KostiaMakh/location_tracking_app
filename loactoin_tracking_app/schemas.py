from datetime import datetime

from pydantic import BaseModel


# MQLProspects
class MQLProspectsBase(BaseModel):
    pass


class MQLProspectsCreate(MQLProspectsBase):
    pass


class MQLProspects(MQLProspectsBase):
    id: int
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    title: str | None = None
    linkedin_url: str | None = None
    company_name: str | None = None
    website: str | None = None
    company_headcount: str | None = None
    location: str | None = None
    industry: str | None = None
    group: str | None = None
    page: str | None = None
    duration: datetime | None = None
    source: str | None = None
    timestamp: datetime | None = None
    session_data: int | None

    class Config:
        orm_mode = True

#
# # SessionData
#
#
# class SessionDataBase(BaseModel):
#     pass
#
#
# class SessionDataCreate(SessionDataBase):
#     pass
#
#
# class SessionData(SessionDataBase):
#     pass
#
#
# # Domain
# class DomainBase(BaseModel):
#     pass
#
#
# class DomainCreate(DomainBase):
#     pass
#
#
# class Domain(DomainBase):
#
#     class Config:
#         orm_mode = True

# from pydantic import BaseModel
