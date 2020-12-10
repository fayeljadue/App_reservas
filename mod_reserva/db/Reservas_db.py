from pydantic import BaseModel
from datetime import date
from typing import Dict

class ReservasDB(BaseModel):

    id_reserva: int
    habitacion: str
    fecha_inicio: date
    fecha_fin: date
    id_quien_realiza: int
    nombre_cliente: str
    apellido_cliente: str
    cedula_cliente: str
    contacto_cliente: str
    estado_reserva: str
    cantidad_personas: int

database_reservas: Dict[int, ReservasDB]

database_users = {
    1: ReservasDB(**{"id_reserva":1,
                       "habitacion":"1, 4, 5",
                       "fecha_inicio":"2020-10-15",
                       "fecha_fin":"2020-10-20",
                       "id_quien_realiza": 43578657,
                       "nombre_cliente": "Carlos",
                       "apellido_cliente": "Lopez",
                       "cedula_cliente": 1012548231,
                       "contacto_cliente": "carlopez@hotmail.com",
                       "estado_reserva": "cancelada",
                       "cantidad_personas": 7
                       }),

    2: ReservasDB(**{"id_reserva":2,
                       "habitacion":"3",
                       "fecha_inicio":"2020-11-01",
                       "fecha_fin":"2020-11-04",
                       "id_quien_realiza": 103879657,
                       "nombre_cliente": "Andrea",
                       "apellido_cliente": "Hernandez",
                       "cedula_cliente": 81254331,
                       "contacto_cliente": "322-874-55-32",
                       "estado_reserva": "completada",
                       "cantidad_personas": 2
                       }),

    3: ReservasDB(**{"id_reserva":3,
                       "habitacion":"1, 2",
                       "fecha_inicio":"2020-12-24",
                       "fecha_fin":"2021-01-02",
                       "id_quien_realiza": 95312578,
                       "nombre_cliente": "Fernando",
                       "apellido_cliente": "Campos",
                       "cedula_cliente": 95312578,
                       "contacto_cliente": "fercam@hotmail.com",
                       "estado_reserva": "pendiente",
                       "cantidad_personas": 4
                       }),

    4: ReservasDB(**{"id_reserva":4,
                       "habitacion":"2",
                       "fecha_inicio":"2020-12-10",
                       "fecha_fin":"2020-12-23",
                       "id_quien_realiza": 85746231,
                       "nombre_cliente": "Armando",
                       "apellido_cliente": "Corrales",
                       "cedula_cliente": 85746231,
                       "contacto_cliente": "armandocorrales@hotmail.com",
                       "estado_reserva": "En progreso",
                       "cantidad_personas": 1
                       }),

    5: ReservasDB(**{"id_reserva":5,
                       "habitacion":"3, 4, 5",
                       "fecha_inicio":"2021-02-20",
                       "fecha_fin":"2021-02-22",
                       "id_quien_realiza": 43578657,
                       "nombre_cliente": "Andres",
                       "apellido_cliente": "Ramos",
                       "cedula_cliente": 1035876759,
                       "contacto_cliente": "anram@hotmail.com",
                       "estado_reserva": "cancelada",
                       "cantidad_personas": 10
                       })
}
