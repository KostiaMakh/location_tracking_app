from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)


Base = declarative_base()


class MQLProspects(Base):
    __tablename__ = 'mql_prospects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    title = Column(String(255))
    linkedin_url = Column(String(255))
    group = Column(String(255))
    page = Column(String(255))
    duration = Column(DateTime)
    source = Column(String(255))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    company = relationship('Company', back_populates='mql_prospects')
    session_data = relationship('SessionData', back_populates='mql_prospects')
    company_id = Column(Integer, ForeignKey('company.id'))

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', 'company_id',  name='_customer_location_uc'),
    )


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(255))
    website = Column(String(255))
    company_headcount = Column(String(255))
    location = Column(String(255))
    industry = Column(String(255))
    mql_prospects = relationship('MQLProspects', back_populates='session_data')


class SessionData(Base):
    __tablename__ = 'session_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(255))
    domain_id = Column(Integer, ForeignKey('domain.id'))
    url = Column(String(255))
    datetime = Column(DateTime)
    city = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))
    latitude = Column(String(255))
    longitude = Column(String(255))
    mql_prospect_id = Column(Integer, ForeignKey('mql_prospects.id'))
    mql_prospects = relationship('MQLProspects', back_populates='session_data')


class Domain(Base):
    __tablename__ = 'domain'

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String(256))