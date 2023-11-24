from pydantic import BaseModel
from typing import List
from datetime import date

class VehicleModel(BaseModel):
    license_plate: str
    color: str
    brand: str
    model: str
    fuel_type: str
    capacity: int
    allow_luggage: bool

class DriverSolicitude(BaseModel):
    id: str
    id_type: str
    name: str
    surname: str
    email: str
    genre: str
    phone: str
    home_address: str
    city: str
    country: str
    birthDate: date
    age: int
    licenseNumber: str
    licenseType: str
    licenseDate: date
    licenseExpirationDate: date

class Solicitude(BaseModel):
    DriverSolicitude: DriverSolicitude
    VehicleModel: VehicleModel
    
    