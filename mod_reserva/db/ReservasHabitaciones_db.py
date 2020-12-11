from pydantic import BaseModel
from datetime import date
from typing import Dict

class ReservasHabitacionesDB(BaseModel):

    id_reserva: int
    id_habitacion: str
    fecha_inicio: date
    fecha_fin: date

database_ReservaHabitaciones: Dict[int, ReservasHabitacionesDB]

database_ReservaHabitaciones = {
    1: ReservasHabitacionesDB(**{"id_reserva":1,
                       "habitacion":1,
                       "fecha_inicio":"2020-10-15",
                       "fecha_fin":"2020-10-20"
                       }),
    
    2: ReservasHabitacionesDB(**{"id_reserva":1,
                       "habitacion":4,
                       "fecha_inicio":"2020-10-15",
                       "fecha_fin":"2020-10-20"
                       }),

    3: ReservasHabitacionesDB(**{"id_reserva":1,
                       "habitacion":5,
                       "fecha_inicio":"2020-10-15",
                       "fecha_fin":"2020-10-20"
                       }),

    4: ReservasHabitacionesDB(**{"id_reserva":2,
                       "habitacion":3,
                       "fecha_inicio":"2020-11-01",
                       "fecha_fin":"2020-11-04"
                       }),

    5: ReservasHabitacionesDB(**{"id_reserva":3,
                       "habitacion":1,
                       "fecha_inicio":"2020-12-24",
                       "fecha_fin":"2021-01-02"
                       }),

    6: ReservasHabitacionesDB(**{"id_reserva":3,
                       "habitacion":2,
                       "fecha_inicio":"2020-12-24",
                       "fecha_fin":"2021-01-02"
                       }),

    7: ReservasHabitacionesDB(**{"id_reserva":4,
                       "habitacion":2,
                       "fecha_inicio":"2020-12-10",
                       "fecha_fin":"2020-12-23"
                       }),

    8: ReservasHabitacionesDB(**{"id_reserva":5,
                       "habitacion":3,
                       "fecha_inicio":"2021-02-20",
                       "fecha_fin":"2021-02-22"
                       }),
    
    9: ReservasHabitacionesDB(**{"id_reserva":5,
                       "habitacion":4,
                       "fecha_inicio":"2021-02-20",
                       "fecha_fin":"2021-02-22"
                       }),

    10: ReservasHabitacionesDB(**{"id_reserva":5,
                       "habitacion":5,
                       "fecha_inicio":"2021-02-20",
                       "fecha_fin":"2021-02-22"
                       })
}