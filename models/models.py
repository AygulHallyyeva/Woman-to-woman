from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime as dt

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    required = Column(String, nullable=False)
    create_at = Column(DateTime, default=dt.now)
    update_at = Column(DateTime, default=dt.now, onupdate=dt.now)
    images = relationship('employeeImages', back_populates='employee')


class employeeImages(Base):
    __tablename__ = 'employee_images'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    create_at = Column(DateTime, default=dt.now)
    update_at = Column(DateTime, default=dt.now, onupdate=dt.now)
    employee = relationship('Employee', back_populates='images')


class Employer(Base):
    __tablename__ = 'employer'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    required = Column(String, nullable=False)
    create_at = Column(DateTime, default=dt.now)
    update_at = Column(DateTime, default=dt.now, onupdate=dt.now)
    image = relationship('employerImages', back_populates='employer')


class employerImages(Base):
    __tablename__ = 'employer_images'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    employer_id = Column(Integer, ForeignKey('employer.id'))
    create_at = Column(DateTime, default=dt.now)
    update_at = Column(DateTime, default=dt.now, onupdate=dt.now)
    employer = relationship('Employer', back_populates ='image')
    