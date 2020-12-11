from pydantic import BaseModel
from datetime import date
from typing import Dict

class ReservasDB(BaseModel):

    id_reserva: int
    id_quien_realiza: int
    nombre_cliente: str
    apellido_cliente: str
    cedula_cliente: str
    contacto_cliente: str
    estado_reserva: str
    cantidad_personas: int

database_reservas: Dict[int, ReservasDB]

database_reservas = {
    1: ReservasDB(**{"id_reserva":1,
                       "id_quien_realiza": 43578657,
                       "nombre_cliente": "Carlos",
                       "apellido_cliente": "Lopez",
                       "cedula_cliente": 1012548231,
                       "contacto_cliente": "carlopez@hotmail.com",
                       "estado_reserva": "cancelada",
                       "cantidad_personas": 7
                       }),

    2: ReservasDB(**{"id_reserva":2,
                       "id_quien_realiza": 103879657,
                       "nombre_cliente": "Andrea",
                       "apellido_cliente": "Hernandez",
                       "cedula_cliente": 81254331,
                       "contacto_cliente": "322-874-55-32",
                       "estado_reserva": "completada",
                       "cantidad_personas": 2
                       }),

    3: ReservasDB(**{"id_reserva":3,
                       "id_quien_realiza": 103879657,
                       "nombre_cliente": "Fernando",
                       "apellido_cliente": "Campos",
                       "cedula_cliente": 95312578,
                       "contacto_cliente": "fercam@hotmail.com",
                       "estado_reserva": "pendiente",
                       "cantidad_personas": 4

                       }),

    4: ReservasDB(**{"id_reserva":4,
                       "id_quien_realiza": 43578657,
                       "nombre_cliente": "Armando",
                       "apellido_cliente": "Corrales",
                       "cedula_cliente": 85746231,
                       "contacto_cliente": "armandocorrales@hotmail.com",
                       "estado_reserva": "progreso",
                       "cantidad_personas": 1
                       }),

    5: ReservasDB(**{"id_reserva":5,
                       "id_quien_realiza": 43578657,
                       "nombre_cliente": "Andres",
                       "apellido_cliente": "Ramos",
                       "cedula_cliente": 1035876759,
                       "contacto_cliente": "anram@hotmail.com",
                       "estado_reserva": "cancelada",
                       "cantidad_personas": 10
                       })
}

def actualizar_reserva(id_reserva: int, estado: str):
    if id_reserva in database_reservas.keys():
        database_reservas[id_reserva].estado_reserva = estado
        return {"Reserva Actualizada": database_reservas[id_reserva]}
    else:
        return "Reserva no encontrada"

def get_idReserva(id_reserva :int):
    if id_reserva in database_reservas.keys():
        return database_reservas[id_reserva]
    else:
        return None

def update_CancelarReserva(id_reserva: int):
        database_reservas[id_reserva].estado_reserva = "cancelada"
        return {"Reserva Actualizada": database_reservas[id_reserva]}
