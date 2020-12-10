from pydantic import BaseModel

class CheckOut(BaseModel):
    id_reserva: int
    estado_reserva: str