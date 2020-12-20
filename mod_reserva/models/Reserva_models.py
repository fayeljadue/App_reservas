from pydantic import BaseModel
from datetime import date
from typing import Dict,List

class CheckOut(BaseModel):
    id_reserva: int

class ReservasCancelado(BaseModel):
      id_reserva: int

class ReservasVisualizar(BaseModel):
    id_reserva: int
    id_quien_realiza: int
    nombre_cliente: str
    apellido_cliente: str
    cedula_cliente: int
    contacto_cliente: str
    estado_reserva: str
    cantidad_personas: int

class ReservasHabitaciones(BaseModel):
    id_reserva: int
    id_habitacion: int
    fecha_inicio: date
    fecha_fin: date

class ReservasVisualzarCompletoOut(ReservasVisualizar):
    lista_habitaciones: List[int]

class CheckIn(BaseModel):
    id_reserva: int
    estado_reserva: str

class UsrLogin(BaseModel):
    usuario: str
    contrasenia: str