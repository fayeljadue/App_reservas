from pydantic import BaseModel
from typing import Dict

class EmpleadosDB(BaseModel):
    id_empleado: int
    nombre: str
    apellido: str
    alias: str
    contrasenia: str

database_empleados: Dict[int, EmpleadosDB]

database_habitaciones = {
    
        43578657: EmpleadosDB(**{"id_empleado":43578657,
                                "nombre":"Antonio",
                                "apellido":"Perez",
                                "alias":"antoperez",
                                "contrasenia":"empperez",
                            }),
        103879657: EmpleadosDB(**{"id_empleado":103879657,
                                "nombre":"Sara",
                                "apellido":"Rodriguez",
                                "alias":"sarodri",
                                "contrasenia":"emprodriguez",
                            }),
}