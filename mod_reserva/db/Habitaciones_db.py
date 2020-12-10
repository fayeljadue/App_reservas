from pydantic import BaseModel
from typing import Dict

class HabitacionesDB(BaseModel):
    numero: int
    habilitada: bool
    tipo: int

database_habitaciones: Dict[int, HabitacionesDB]

database_habitaciones = {
        1: HabitacionesDB(**{"numero":1,
                             "habilitada":True,
                             "tipo":1,
                            }),
        2: HabitacionesDB(**{"numero":2,
                             "habilitada":False,
                             "tipo":2,
                            }),
        3: HabitacionesDB(**{"numero":3,
                             "habilitada":True,
                             "tipo":2,
                            }),
        4: HabitacionesDB(**{"numero":4,
                             "habilitada":False,
                             "tipo":3,
                            }),
        5: HabitacionesDB(**{"numero":5,
                             "habilitada":True,
                             "tipo":4,
                            })
}