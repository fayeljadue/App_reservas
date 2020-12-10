from pydantic import BaseModel
from typing import Dict

class TiposHabitacionesDB(BaseModel):
    id_tipo: int
    nombre: str
    capacidad: int
    precio: int
    extras: str

database_tipos_habitaciones: Dict[int, TiposHabitacionesDB]

database_habitaciones = {
        1: TiposHabitacionesDB(**{"id_tipo":1,
                                  "nombre":"Lujo multiple",
                                  "capacidad":4,
                                  "precio":150000,
                                  "extras":"Jacuzzi, Room service 24h, Estacionamiento vigilado, Traslado al aeropuerto, Bar",
                                }),
        2: TiposHabitacionesDB(**{"id_tipo":2,
                                  "nombre":"Lujo doble",
                                  "capacidad":2,
                                  "precio":80000,
                                  "extras":"Jacuzzi, Room service 24h, estacionamiento vigilado, Traslado al aeropuerto, Bar",
                                }),
        3: TiposHabitacionesDB(**{"id_tipo":3,
                                  "nombre":"Estandar multiple",
                                  "capacidad":4,
                                  "precio":90000,
                                  "extras":"Estacionamiento vigilado, Traslado al aeropuerto",
                                }),
        4: TiposHabitacionesDB(**{"id_tipo":4,
                                  "nombre":"Estandar doble",
                                  "capacidad":2,
                                  "precio":50000,
                                  "extras":"Estacionamiento vigilado, Traslado al aeropuerto",
                                }),
}