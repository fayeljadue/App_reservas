from pydantic import BaseModel
from datetime import date
from typing import Dict

class ReservasHabitacionesDB(BaseModel):

    id_reserva: int
    id_habitacion: int
    fecha_inicio: date
    fecha_fin: date

database_ReservaHabitaciones: Dict[int, ReservasHabitacionesDB]

database_ReservaHabitaciones = {
    1: ReservasHabitacionesDB(**{"id_reserva":1,
                       "id_habitacion":1,
                       "fecha_inicio":date(2020,12,11),
                       "fecha_fin":date(2020,10,20)
                       }),
    
    2: ReservasHabitacionesDB(**{"id_reserva":1,
                       "id_habitacion":4,
                       "fecha_inicio":date(2020,10,15),
                       "fecha_fin":date(2020,10,20)
                       }),

    3: ReservasHabitacionesDB(**{"id_reserva":1,
                       "id_habitacion":5,
                       "fecha_inicio":date(2020,10,15),
                       "fecha_fin":date(2020,10,20)
                       }),

    4: ReservasHabitacionesDB(**{"id_reserva":2,
                       "id_habitacion":3,
                       "fecha_inicio":date(2020,11,1),
                       "fecha_fin":date(2020,11,4)
                       }),

    5: ReservasHabitacionesDB(**{"id_reserva":3,
                       "id_habitacion":1,
                       "fecha_inicio":date(2020,12,24),
                       "fecha_fin":date(2021,1,2)
                       }),

    6: ReservasHabitacionesDB(**{"id_reserva":3,
                       "id_habitacion":2,
                       "fecha_inicio":date(2020,12,24),
                       "fecha_fin":date(2021,1,2)
                       }),

    7: ReservasHabitacionesDB(**{"id_reserva":4,
                       "id_habitacion":2,
                       "fecha_inicio":date(2020,12,10),
                       "fecha_fin":date(2020,12,23)
                       }),

    8: ReservasHabitacionesDB(**{"id_reserva":5,
                       "id_habitacion":3,
                       "fecha_inicio":date(2021,2,20),
                       "fecha_fin":date(2021,2,22)
                       }),
    
    9: ReservasHabitacionesDB(**{"id_reserva":5,
                       "id_habitacion":4,
                       "fecha_inicio":date(2021,2,20),
                       "fecha_fin":date(2021,2,22)
                       }),

    10: ReservasHabitacionesDB(**{"id_reserva":5,
                       "id_habitacion":5,
                       "fecha_inicio":date(2021,2,20),
                       "fecha_fin":date(2021,2,22)
                       })
}

def buscar_reserva_rango_f(f_ini_bus:date,f_fin_bus:date):
    """
    Funcion que permite buscar dentro de una rango de fechas una reserva y retorna los ids
    """
    reservas_habitaciones=list()
    reservas_id = set()
    for reserva_habitacion in database_ReservaHabitaciones.items():
        fecha_inicio=reserva_habitacion[1].fecha_inicio
        fecha_fin=reserva_habitacion[1].fecha_fin
        if(f_ini_bus<=fecha_inicio<=f_fin_bus or f_ini_bus<=fecha_fin<=f_fin_bus):
            reservas_habitaciones.append(reserva_habitacion)
            reservas_id.add(reserva_habitacion[1].id_reserva)
    if len(reservas_habitaciones) == 0:
        return None,None
    return reservas_id,reservas_habitaciones

def get_fecha_inicio(id_reserva: int):
    if id_reserva in database_ReservaHabitaciones.keys():
        prueba = database_ReservaHabitaciones[id_reserva].fecha_inicio
        print(prueba)
        return database_ReservaHabitaciones[id_reserva].fecha_inicio
    else:
        return None